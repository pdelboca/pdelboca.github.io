title: Zero Downtime: Self-Hosting Open Source solutions is reliable.
date: 2026-01-05

![alt text](/static/imgs/uptime.png)

## Self Hosting our Big Blue Button instance

At the [Open Knowledge Foundation](https://okfn.org/en/) we self-host our own instance of Big Blue Button. We use it for meetings and to host public webinars and events (some times with 100+ people connected at a time).

As a part of new year refresh I upgraded from 2.7 to 3.0 and here are some interesting points:

1. The Virtual Machine and the application has been up since I created it: 279 days ago. **No downtime**.
3. Installing it took me less than a day (most of the time getting familiar with the product, the install itself took less than an hour). Upgrading it took me less than a morning.
5. During these last 9 months we didn't have any problem.
6. During these last 9 months we **had more downtime of Slack than our self-hosted BBB**.
7. During these last 9 months I didn't spend a single minute maintaining it.
8. Security upgrades on the server are applied automatically by default thanks to unnatended-upgrades package.
9. Of course, no critical vulnerability was detected on BBB, therefore, no need for manual interventions.
10. Hosting it cost just **€23 a month for all of the organization** (in comparison to around €10 a month per user).

For me is not at all a surprise (I have been around since before the cloud and the boom of SaaS) but nowadays it seems that a service running without interruptions for a year is only possible with some kind of cloud service or SaaS. That's not the case, you can have your own server running your own software for as long as the machine is on, it is more simple than we are being told.

Of course SaaS and Cloud has its benefits for some particular scenarios, but sadly they are cascading its complexity and prices into day-to-day software that should be more affordable and simple. <mark>99.9% of availability is not exclusive of cloud or SaaS software, it can be achieved by just self-hosting your application.</mark>

