# Voiceover Script: Scaling Without Fracturing (Nutanix OrgDNA Analysis)

This is the pacing script for your 10-minute OB2 video memo. Read this at a steady, conversational pace.

Hello. My name is Parag. Today, I’ll be presenting an organizational analysis of a critical failure—and subsequent turnaround—during a high-stakes engineering project at Nutanix. We’ll be looking at why four exceptional engineering teams failed to deliver a critical migration product on time, and how applying the OrgDNA framework revealed the root causes.

Before we get into the organization, we have to understand the stakes. When Broadcom acquired VMware, they dismantled legacy licensing agreements. Millions of enterprise customers suddenly had a two-year ticking clock before their infrastructure costs skyrocketed. 

For Nutanix, this was a once-in-a-decade window. These were Fortune 500 customers with fifty to one hundred million dollar deal sizes. But to win them, we needed to build a seamless migration tool that could lift-and-shift their entire infrastructures from VMware to Nutanix. Time was of the essence. If we were late, those customers would be forced to lock into expensive new VMware contracts or look elsewhere. Nutanix would be locked out for a decade.

So what was our mission? We had to build 'Nutanix Move'—an automated hypervisor migration product. 

The complexity was staggering. We weren't just moving files; we were translating live network topologies and storage architectures across competing platforms with zero margin for error. 

But the real barrier wasn't technical. Despite having top-tier talent, the project immediately hit severe delays. Deadlines slipped by weeks. Integration testing resulted in cascading failures. I needed to find out why.

Our product required deep integration across four distinct teams, but we had zero shared North Star. 

On one side, you had three deep functional silos: The Core AHV Team, the Networking Team, and the Uhura ESXi team. Their KPIs were entirely inwardly focused—building native features and maintaining raw stability. Because of this, they pushed away orchestration responsibility, denied ownership of cross-node routing, and viewed migration as 'just another workload.'

On the other side was my team, the Move Team. We were the Orchestrators. Our sole KPI was end-to-end delivery velocity. We were attempting to push the boulder uphill and coordinate all teams, but we lacked the formal authority to force prioritization. Every team was measured on their outcome—not the customer's outcome.

To understand why this was happening, I applied the OrgDNA framework from our Organizational Behavior coursework. Specifically, I broke the failure down into three dimensions: Architecture, Culture, and Power & Influence. What I found was a system perfectly designed to produce the delays we were experiencing.

Let’s start with Architecture. Our formal structure was built on deep, functional silos without a shared North Star. 

The absolute root cause of our delays was massive 'structural holes' between the four teams. We did not share a VP. Each team reported up an entirely different chain. To get true alignment on a common goal, decisions technically had to escalate all the way up to the CTO.

Meanwhile, execution was happening four levels down from that. Day-to-day work sat with engineers and managers like myself. But because engineers were incentivized strictly on isolated functional stability, any cross-team interface dispute required a multi-layer escalation: from Engineer, to Manager, to Director, to Senior Director, and finally to VP. This sheer vertical distance meant a technical disagreement that should have taken an hour to resolve added weeks to our timeline. It was a classic 'blind men and the elephant' problem.

Next, I looked at our Culture. We had inadvertently fostered an environment of 'Deflection and Blame Shifting.'

Instead of taking joint responsibility, teams actively shifted blame to other functional silos when things failed. A massive avoidance tactic emerged: whenever the Move team highlighted an integration failure, the gatekeeping teams would endlessly demand that we 'reproduce the issue' on our own before they would even look at it. They stalled to delay taking ownership.

Why? Because implicitly, accepting a cross-functional problem damaged your own team's reputation. Deflection wasn't a flaw in our people; it was an ingrained survival habit. As we learned from the NUMMI case, you cannot change culture by telling people to think differently. You have to change what they do every day.

Finally, we analyzed Power dynamics. There was a severe imbalance acting as a bottleneck.

The Core Platform and AHV teams held the complex, legacy codebase. They became structural gatekeepers. Meanwhile, the UX and Edge teams had to wait for upstream APIs to be finalized. This created a high degree of asymmetric dependency.

Because the Core engineers had more referential expertise and structural power, upstream delays were often dismissed as 'necessary complexity,' while downstream teams bore the brunt of the schedule slipping. We needed to flatten this power gradient so that downstream teams had voice and visibility without having to beg for API access.

So, how did we fix this? We moved beyond the formal organizational chart and completely rewired the DNA. The recommendation was what we called the 'Squad Shift.'

Architecturally, we formed a dedicated cross-functional squad led by a single Product DRI with authority over the end-to-end outcome, closing those structural holes.

Culturally, we had to shift the norm to align incentives and drive collective accountability. We deployed a 'carrot and stick' approach. For the carrot, we introduced an excellence system where managers and peers from other teams can formally recognize exceptional cross-functional contributions. For the stick, we added the shared project directly into the OKRs of all participating teams, so that any delays reflect equally on everyone's performance.

And from a Power perspective, we created mutual dependence. We formally recognized cross-functional broker roles and deployed a unified dashboard across all teams, breaking the monopoly of the gatekeeper teams by making all dependencies and blockers completely transparent.

Implementing this required a phased approach.

Phase 1 is 'Building Awareness & Forming Leadership.' We don't just start with engineers; we start at the top. We build awareness across the organization from the CTO, VPs, and Product Managers to ensure this initiative is explicitly prioritized on every single team's roadmap. Only then do we identify and form the cross-functional leadership squad by pulling leads from each of the four teams.

Phase 2 is 'Prove Value & Build the Case.' We introduced rapid collaborative huddles to demonstrate early wins, like shorter dependency-resolution times, and used pilot data to build the case for a broader rollout.

Phase 3 is 'Institutionalise & Reward.' We revised the incentive structures with HR so that manager performance reviews are strictly tied to cross-functional outcomes, institutionalizing our new 'carrot and stick' mindset.

With any structural change, we have to anticipate the obstacles to bullet-proof our strategy. 

We foresee four primary risks spanning architecture, culture, and power. 

Architecturally, role conflicts will predictably emerge between the new cross-functional squad leads and legacy functional managers. To mitigate this, we define a strict mandate: the squad owns the "What", and functional managers own the "How".

Culturally, there is a risk that teams ignore the new "carrot" recognition system. We prevent this by embedding cross-team recognition directly into mandatory quarterly review templates.

From a power perspective, the highest likelihood risk is that under deadline pressure, VPs revert to functional protectionism. To bullet-proof this, the CTO must strictly enforce the "stick"—weighting shared OKRs above all functional KPIs in executive performance reviews. We can't just change the engineers' incentives; we must change the executives' incentives too.

Finally, increased dashboard transparency might trigger defensiveness. We mitigate this through explicit executive air cover: leadership must exclusively use the unified dashboard in weekly reviews, refusing to acknowledge hidden back-channels.

We will know this is working by tracking three specific metrics:
1. Operational: A fifty percent reduction in cross-team dependency resolution time.
2. Customer: Sustaining our core strength 90+ Net Promoter Score throughout these complex migrations.
3. Cultural: An increase to 3–5 proactive escalations per sprint—a leading indicator that our engineers finally feel psychologically safe enough to flag problems.

In conclusion, Nutanix's migration project was fundamentally at risk, not because of a failure of technology, but because our DNA was built for functional excellence—not cross-functional delivery.

We had the right talent and the right vision entirely. What was missing was the organizational system designed to let four distinct teams move as one. By restructuring our architecture, reshaping our culture through shared consequences and rewards, and balancing power, we can finally capitalize on this once-in-a-decade market window.

Thank you for your time.
