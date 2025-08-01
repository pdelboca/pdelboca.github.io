title: vibe coding is the fast fashion industry of software engineering
date: 2025-08-01

**TL;DR**: My take on AI for programming and "vibe coding" is that it will do to software engineering what fast fashion did to the clothing industry: flood the market with cheap, low-quality products and excessive waste.

First, to get this out of the way, I’ll note that I’m a casual user of LLMs for coding. I don’t use agents or AI-powered IDEs, but a couple of times a week, I use LLMs for two things: cheaply testing ideas and debugging. I’ve never found LLM-generated solutions reliable enough to fix issues in my production codebases, but they are sometimes helpful in my thought process. For me, AI has simply replaced the shitty experience of current web-searching for solutions.

## Current State
LLMs excel at producing low-quality code (more on this later) that kinda works for a given prompt. In my experience, LLM-generated code typically:

 * lacks basic optimizations and good practices,
 * due to how they’re built, LLMs provide code based on outdated versions (which may contain security vulnerabilities)
 * The codebase lacks design or architectural considerations and
 * whatever the output is, it fails in complex scenarios.

Yet, this doesn't change the fact that LLMs do produce code, that the code it produces do solve some basic needs and it is quite accessible. Recently, I asked an LLM to create files for deploying an R Shiny app behind a Caddy web server with basic auth. Within minutes, I had a Docker Compose file with a "Hello World" ready to run. I tested it, confirmed hypotheses, deleted the files, and moved on. The tool’s ability to write code easily is undeniable and it is here to stay.

## Don’t Build It
I once [read](https://mitgovlab.org/resources/dont-build-it-a-guide-for-practitioners-in-civic-tech/): "The problem with software is that anything can be built." and I couldn't agree more. This lack of constraints is what causes bloated applications, overengineered frameworks, code waste, and shitty apps. Vibe coding will exacerbate this flaw, is going to put steroids on this coding monster that just adds features and layers of complexity just because it is possible "and fun" to do it.

I have been a Open Source developer and maintainer for more than a decade and I'm at that point in which I understand that more code is not always the solution. It is clear for me that a new feature not only has a potential value but it also adds maintainance cost. Sometimes code is not an asset but a liability. When I was a kid whenever I walked around fancy neighborhoods I would ask my mom: *"Look at that big house, don't you want one?"* just to get a straight answer: *"And who is gonna clean it?"*. Oh mom how I understand you now! Whenever someone suggest to add something cool to a software I echo her: *"And who is going to maintain it?"*

## Food for thoughts

As code production cheapens, we should examine parallels in other industries and my mind automatically goes to fast fashion: cheaper production led to affordable but low-quality clothes that are cheaper to discard than reuse or even repair. Similarly, I foresee a future of cheap software flooding the market, polluting ecosystems, and harming users. The key difference? In fast fashion, a flawed product means throwing out running shoes after two races; in software, it means sensitive data from thousands of women becoming public, as with the recent [Tea app leak](https://www.nytimes.com/2025/07/26/us/tea-safety-dating-app-hack.html).

Cheaper production is often hailed as progress, but when the result is waste that can’t be reused or repaired, overproduction becomes a problem. One could argue LLMs can aswell "repair" code cheaply, but realistically, no LLM will swiftly patch a Log4j vulnerability. We’re headed toward an internet polluted by low-quality code. Choose your own adventure: cheaper and affordable software or an unsustainable, ecosystem-polluting nightmare. A last note, I'm not only talking about ecological pollution but also on the noise pollution that so much shitty code will create. High quality software (whatever that means) will be harder to get if you do not know where to look.

## Formal Definitions

In the age of verbose coding machines, we need formal definitions. One of the reasons why the public debate around LLMs use for coding is extremelly opinionated and hyped is because up to this point our community still struggles with some basic definitions of terms like: "simple software", "good quality code", "maintainable code", "reusable", etc. There’s no widely adopted metric to evaluate code quality produced by either developers or LLMs. We must evolve beyond an LGTM-driven industry to professional standards. I don’t know why these definitions elude us, but they’re urgently needed.

I won’t scare developers with words like "certifications" or "licenses to practice", but as poor-quality code proliferates, proving our work’s quality will become critical. As data leaks and breaches increase, accredited providers or certified professionals will gain importance. And don't be confused, if a disaster happens the responsibility will always be on person, never the machine: AI will take all the credits and developers the blame.

