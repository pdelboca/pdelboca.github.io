title: rebuilding the wheel: my static site generator
date: 2025-06-01

### A 200-lines Python script to render my personal website.

Lately I feel like I want to start writing again but I get stuck in the publishing part of it in a constant look of finding the right tool for it. I tried several Static Site Generators out there but I couldn't found any that fits my **quarks** so I decided to give it a try and create one my own. One rule: simple enough to get me up and running again.

Things I want:

  - My website to look like a website and not like a blog: Home page, About, Projects, Blog.
  - To be able to customize the look and feel using tools I know: HTML and CSS.
  - I write a lot for external blogs, so I want to also list all the external content.
  - Store the content of my website in Markdown.
  - Minimal dependencies so I don't botter updating packages every 6 months.
  - Keep hosting and old static sites from the days where I used to blog using RMarkdown.

Thigs I do not care about:

  - Comments section.
  - RSS Feed.
  - Social media integration.
  - Tags and categories.
  - Search.

Basic architecture:

  - `static/` for CSS and all the files of my old site.
  - `content/` folder with Markdwon files stored in `YYYY/MM/DD` folder.
  - `template/` folder with a bunch of templates.
  - `docs/` folder to host the static site (for Github publishing)
  - `main.py` file to read the content using `markdown` library and render the website using `jinja2`.
  - Push to Github repository to host the static website

**For the processing part:** I decided to go with a really simple Python script that uses `markdown` to read the contents and `jinja2` to render the website. With the help of a junior AI assistant I was able to get it done in less than an hour since the concept is quite easy:

 - Iterate through the content folder.
 - Use `markdown` library to read the files.
 - For every blogpost create a context object with some metadata.
 - Pass the context object to `jinja2` render function.

**For the front end:** I reused some HTML and CSS that I had and created the `jinja2` templates. Since the website is quite minimalistic this was quite straight forward since it follows the same pattern of every Flask/Djando application:

 - A base.html file for loading styles and boilerplate HTML code.
 - One template for every page: index, about, projects.
 - A template for listing all the writings (the name I chose for my blogs)
 - A template for every single writing.

The resulting project needs a little bit of polishing but I was able to get my own Static Site Generator in less than 200 lines of python ([link to the repository](https://github.com/pdelboca/pdelboca.github.io)).

Now, hopefully, I can start writting and publishing again...
