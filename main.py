import os
import re
import markdown
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def parse_metadata_and_content(md_text):
    metadata = {}
    lines = md_text.split('\n')
    content = []
    metadata_end = False

    for line in lines:
        if not metadata_end:
            match = re.match(r'^(\w+):\s*(.*)$', line)
            if match:
                key = match.group(1).lower()
                value = match.group(2)
                metadata[key] = value
            else:
                metadata_end = True
                if line.strip() != '':
                    content.append(line)
        else:
            content.append(line)

    return metadata, '\n'.join(content).lstrip()

def process_writings(template_env, public_dir):
    writings = []
    content_writings_dir = os.path.join('content', 'writings')

    for root, dirs, files in os.walk(content_writings_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, content_writings_dir)
                path_parts = rel_path.split(os.sep)

                if len(path_parts) < 4:
                    continue  # Skip files not in YYYY/MM/DD structure

                year, month, day, filename = path_parts[0], path_parts[1], path_parts[2], path_parts[3]
                date = datetime(int(year), int(month), int(day))

                with open(full_path, 'r', encoding='utf-8') as f:
                    md_text = f.read()

                metadata, content = parse_metadata_and_content(md_text)
                is_external = 'url' in metadata
                title = metadata.get('title', 'Untitled')
                html_content = markdown.markdown(content)

                if not is_external:
                    # Generate individual post page
                    output_dir = os.path.join(public_dir, 'writings', year, month, day)
                    os.makedirs(output_dir, exist_ok=True)
                    output_filename = os.path.splitext(filename)[0] + '.html'
                    output_path = os.path.join(output_dir, output_filename)

                    post_url = f'/writings/{year}/{month}/{day}/{output_filename}'
                    writing_template = template_env.get_template('writing.html')
                    rendered = writing_template.render(
                        title=title,
                        content=html_content,
                        date=date.strftime('%B %d, %Y')
                    )

                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(rendered)
                else:
                    post_url = metadata['url']

                writings.append({
                    'title': title,
                    'url': post_url,
                    'date': date,
                    'is_external': is_external
                })

    # Sort writings by date descending
    writings.sort(key=lambda x: x['date'], reverse=True)

    # Render writings listing page
    writings_template = template_env.get_template('writings.html')
    rendered = writings_template.render(writings=[
        {
            'title': w['title'],
            'url': w['url'],
            'date': w['date'].strftime('%Y-%m-%d'),
            'is_external': w['is_external']
        }
        for w in writings
    ])

    with open(os.path.join(public_dir, 'writings.html'), 'w', encoding='utf-8') as f:
        f.write(rendered)

def process_projects(template_env, public_dir):
    projects_md = os.path.join('content', 'projects.md')
    if not os.path.exists(projects_md):
        return

    with open(projects_md, 'r', encoding='utf-8') as f:
        md_text = f.read()

    metadata, content = parse_metadata_and_content(md_text)
    html_content = markdown.markdown(content)

    projects_template = template_env.get_template('projects.html')
    rendered = projects_template.render(
        title=metadata.get('title', 'Projects'),
        content=html_content
    )

    with open(os.path.join(public_dir, 'projects.html'), 'w', encoding='utf-8') as f:
        f.write(rendered)

def main():
    public_dir = 'public'
    os.makedirs(public_dir, exist_ok=True)

    # Set up Jinja2 environment
    template_env = Environment(loader=FileSystemLoader('templates'))
    template_env.trim_blocks = True
    template_env.lstrip_blocks = True

    # Process core pages
    process_writings(template_env, public_dir)
    process_projects(template_env, public_dir)

    # Render index page
    index_template = template_env.get_template('index.html')
    with open(os.path.join(public_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_template.render())

if __name__ == '__main__':
    main()
