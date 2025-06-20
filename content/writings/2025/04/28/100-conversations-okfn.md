title: 100+ conversations: #thetechwewant
date: 2025-04-28


### What we need is concrete tech for the people who need it, and nothing else

_Originally posted on [OKFN's Blog](https://blog.okfn.org/2025/04/28/patricio-del-boca-what-we-need-is-concrete-tech-for-the-people-who-need-it-and-nothing-else/)_

**Let's start with the basics. What is the problem with the software being developed by Big Tech today?**

It is important to distinguish between two things when answering this question. One is the products that Big Tech sells, and the other is the tools that they develop and that influence software development worldwide. I will focus on the latter.

Since the popularisation of the Internet and digital technologies, companies like Google have faced a very specific problem: how to get billions of people to access their websites. Google, for example, had a search engine that wanted to index the entire Internet. Facebook and Twitter have to deal with millions of daily posts, YouTube and Netflix have to store and transmit terabytes of video information, and so on. To solve these problems of scale, these companies started to develop tools and frameworks that ended up being open source.

In the era of big data, these large companies had to develop technologies and ways of working to meet the demand for consumption (and growth) of their platforms. Some examples: microservices, infrastructure as code, indexing engines, APIs or Kubernetes. Unfortunately, this boom in technologies that solved specific problems for this 5% of technology companies had two very negative consequences: it distanced development from the basic architecture of the web (servers communicating via HTTP and exchanging HTML) and it hypnotised the technology community, which began to adopt these tools for all its developments, even though they do not have billions of users and do not face similar challenges.

The software world absorbed these technologies, but without having to solve the same problems. The normal everyday software that someone has in my local hardware store, my local supermarket or my local council does not have these problems. So if the vast majority of the world's software doesn't need the scale of Facebook, Google or Twitter, why should it need the same tools, technologies and ways of working?

That's where we are now, with very few initiatives or companies that really need or have big data, but have used these tools because it was modern, it was new, it was marketing. Because they didn't want to miss out on the 'innovation wave'. I repeat myself: Silicon Valley companies and my city council don't have the same needs or the same resources, so why should they use the same tools?

All this has led to the current situation and to the point I want to defend: there is over-engineering in the world of digital technologies. 95% of companies do not have the same problems as Facebook, Twitter, Google or Amazon, using the same solutions and the same tools is completely unsustainable. I don't need a 4x4 to go shopping. An SUV is designed to pull a 3-ton tractor out of the mud. If I use it just to carry shopping bags I'm overpaying for something that costs a lot more to produce and consumes a lot more and whose potential goes unused: the perfect definition of unsustainable consumption.

**It's funny that you use the SUV analogy, because a few months ago I read the news that the city of Paris held a referendum to ask the citizens if they should multiply the cost of parking SUVs in the city centre. And the people said yes, multiply the taxes for those who use SUVs where they shouldn't. So I ask: how should we deal with SUV parking in the city centre? So I ask: how should we deal with the over-engineering of software today? With regulation? With taxes?**

I think there are several tools, there are many fronts and there is no single silver bullet to solve this. Regulation is clearly one way, and the state has a role that it is not fulfilling. We need to focus on regulating commercial practices such as pre-sales (which is nothing more than lobbying) and vendor lock-in (because the technology is proprietary, the buyer is tied to the developer). One possible solution is for states to use free software, not only for technological reasons, but also for reasons of sovereignty and security. But there is also a cultural and technological change that needs to take place, especially in the technology community, where voices are beginning to be heard today talking about these issues.

I always give two points of reference. One is this new project that has recently emerged: HTMX, which is a small library for web development that extends the functionality of HTML. You don't need a whole complex framework to build most web pages, let's go back to basics: HTML and a backend is enough. The other reference is Ruby on Rails, a simple framework where a developer can only take care of the backend and the frontend. Ruby on Rails has in its design this idea of the 'renaissance developer' who is able to build a product in its entirety. Fortunately, we are slowly (again) creating ecosystems of tools that allow a single person to be efficient and create sustainable solutions.

Technological innovation' and technological overkill have been top-down because it didn't start with "I've got a developer, what can I do with him/her", it started in Silicon Valley with "I've got millions of dollars, what do I want to do?" That's how a lot of the tools have become very expensive and are used to solve the problems of the 1%.

Another front we can attack is hardware. Hardware has come a long way in the last 20 years. A Raspberry Pi alone now has the same processing power as many servers from two decades ago. You no longer need 'the cloud' to scale and grow, today's servers that can be installed locally have enough power for most of the applications we need.

So, in summary, over-engineering can be solved on several fronts: government regulation so that they do not sell smoke to the state, reviewing the capabilities of modern hardware as an option to the cloud, and cultural change in the technology community to produce more sustainable tools.

**I was a bit surprised that in the first question, about the problem of mainstream software, you didn't fall into the open vs. closed dichotomy. I would like to expand on that. Even when we talk to multilateral organisations with a clear public interest, such as the UN or the G20, to give a few examples, it is not obvious that their technological solutions have to be open and free. There is concern and resistance, even from people who are theoretically on the side of power. Why is that? Why should open source be the standard? What are the technical advantages? How do you get around the issues of security, privacy, effectiveness, etc. that seem to create resistance?**

Yes, there is a lot of unfounded resistance, but there is also a historical reality that has favoured the development of private solutions over open solutions. Today it is true that there are private solutions that are better than open ones because they have had more inertia, they have been first to market, they have had more investment and therefore they work better. For some problems, there are only private solutions that work, and we have to accept that. I think this context is the initial source of resistance to open source: it is still in the collective unconscious that free software is less beautiful, more difficult and less intuitive than private software.

Beyond this 'fame', more on the technical side, I think the reluctance is also based on the notion of 'security by secrecy'. That is, that software is more secure because nobody knows about it - which is necessarily true. Keeping something secret does not mean that it is more secure, I would say the opposite. Recently there was a case where an open encryption technology used for banking transactions was hacked. There was a bug, it affected a lot of people, but it was discovered, fixed and modified in a very short time, precisely because it is open. The idea that open software is insecure because everyone knows the source code is wrong, because while there are two eyes trying to loot it, there are 20 other eyes in the open development community trying to make it more secure.

And, of course, proprietary software is the source of what we were talking about earlier, the issue of power and control. It ties the buyer to the vendor and its supply chain. Audits are contracted to certify that the proprietary software is secure, specialised teams trained by this or that company are contracted, and so on. In the end, it's always going to be a matter of trust, because if you don't open the code, you'll never know if it's really secure. You have to trust someone who says it is secure.

If anything, I think in the last five years the ecosystem has changed a bit. The digital infrastructure of the world today is built on Linux. The servers of most web servers are free, the same goes for Android, and so on. In other words, it has been shown that free software is much more robust than it is often given credit for.

**The concept of public software, or public code, is being used a lot nowadays. From there, the notion of public digital infrastructure (DPI) was developed, which was put on the global agenda at the last G20 meeting in India, and which has become the focus of attention of many organisations, starting with our own, the Open Knowledge Foundation. Such a concept does not by design carry the adjective “open”. Do you think all DPI should be open, and why?**

Yes, it should. Firstly, because it is public. If the digital infrastructure is public, then everyone should have the right to see it, understand it, update it, use it and check it. Just like a public square: I have the right to enter and enjoy it.

Then for the sake of transparency. Not only is what the software does transparent, but so is the bidding process. If you have open software, you remove the interest of making you a slave to a closed solution or selling you 'exclusivity'. If the tool is open, then the best and cheapest user wins. Full stop.

Also because of the innovation issue. With open software, there is a whole ecosystem that has access and can innovate: universities, independent communities, social organisations and also the private sector. We have to get away from this dichotomy that innovation only comes from the private sector. If the only thing that drives us to innovate is money, we have a problem as a society.

Another reason is cost. Open software allows reuse, which reduces costs. We need to stop reinventing the wheel and share solutions, improve them, etc.
Which brings us to another related reason: sustainability. Private software involves hundreds of developers in dozens of different companies doing the same thing. This wastes resources, ties the buyer (in this case the government) to one company, and is ultimately inefficient in terms of human and natural resources. Open source software is reusable and therefore more sustainable in the long run.

Finally, of course, there are the communities. Open infrastructures create a community ecosystem with enormous benefits, as we discussed earlier. It is more than clear that open source software has 25,000 more benefits than private software in the state.

**Elections are a topic you are passionate about. Your most practical experience is at the local level with Open Data Cordoba, such as the alternative vote counting system and other election initiatives. What is your vision for scaling these kinds of open, community-based, bottom-up solutions? Or rather, should they be scaled up? And how?**

Yes, yes, I think they should be scaled. But scale in the sense of reusing solutions, not in the sense of increasing the adoption of the same centralised technology. One of the great advantages of working with elections is that, despite the particularities of each country, they are all more or less the same. At the end of the day, it's about electing somebody, counting the votes, registering the people who voted and publishing the results. So there is a lot of scalability.

The concept of public digital infrastructure is perfect in that sense, because it focuses on building small interoperable solutions that can be reused and clustered to solve specific local problems. Rather than each community or country developing its own tools, it is much more efficient to share the same modular and interoperable infrastructure, and to evolve the software and protocols with the different experiences and learnings from each place. This is the goal of our project.

I am convinced that communities, and the Open Knowledge Network in particular, are the ideal engines for this. The experience we have had over the last year of holding roundtables in different continents and contexts, unintentionally and unplanned, has shown us that all countries have similar solutions to similar problems. In Italy, a small town in the south of Sicily has the same problem as my province in Cordoba, Argentina. In other words, let's communicate and collaborate to scale, as I said, in the sense of reusing the open technologies that exist and those that we will create together. To scale is to collaborate.


**Since last year, with the development of the Open Data Editor (ODE), we've been trying to put all this into practice and, in a way, lead by example, showing that a different approach to technology is possible. How are you and our technology team applying The Tech We Want principles to the creation of this application?**

The Open Data Editor was created with the intention of making the full capabilities of the Frictionless Data project (which consists of a fairly technical collection of standards and specifications for working with open data) available to people without any knowledge of coding or programming languages. There are lots of people out there, activists, civil servants and small social organisations, who don't need complex software to clean up their spreadsheet data and correct errors. So the first task was to simplify ODE's architecture as much as possible and make it easy to use, run offline, run operations locally with privacy rather than in the cloud, and provide data training in an accessible way through a free online course.

This year, we are focusing on energising the community around the app and exponentially increasing adoption among the groups we see as key: activists, social organisations and governments. We are already working closely with five pilot organisations from a first cohort, and will soon be launching a call for a second cohort. The emerging use cases for the Open Data Editor are impressive. Take a look at the work of the Observatoire des armaments on the war industry in France and you will understand the impact that a simple and accessible tool like ODE can have, and the difference it makes to a small but strong and committed team.

**Let's summarise: What technologies do we want and what technologies do we need?**

We want technologies that are accessible. By accessible, I mean open and cheap, whose innovation and development are not tied to large corporations. What's more, we want them to be sustainable. In other words, the technology we build today won't need to be rewritten in two years' time and won't require entire teams to maintain.


**And for whom are we building these technologies?**

We need concrete technologies for people who need them, based on real needs, not on oversized problems. Nothing else.
