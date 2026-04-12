# Voiceover Script: Scaling Without Fracturing (Nutanix OrgDNA Analysis)

This is the pacing script for your 10-minute OB2 video memo. Read this at a steady, conversational pace, remembering to pause slightly after advancing each slide to let the visual elements settle.

---

### [Slide 1: Title Slide]
**(0:00 - 0:20 | 20 seconds)**
"Hello. My name is Parag Rahangdale from Section A7. Today, I’ll be presenting an organizational analysis of a critical failure—and subsequent turnaround—during a high-stakes engineering project at Nutanix. We’ll be looking at why four exceptional engineering teams failed to deliver a critical migration product on time, and how applying the OrgDNA framework revealed the root causes."

*(Advance to Slide 2)*

---

### [Slide 2: The Stakes (Burning Platform)]
**(0:20 - 1:20 | 60 seconds)**
"Before we get into the organization, we have to understand the stakes. When Broadcom acquired VMware, they dismantled legacy licensing agreements. Millions of enterprise customers suddenly had a two-year ticking clock before their infrastructure costs skyrocketed. 

For Nutanix, this was a once-in-a-decade window. These were Fortune 500 customers with fifty to one hundred million dollar deal sizes. But to win them, we needed to build a seamless migration tool that could lift-and-shift their entire infrastructures from VMware to Nutanix. Time was of the essence. If we were late, those customers would be forced to lock into expensive new VMware contracts or look elsewhere. Nutanix would be locked out for a decade."

*(Advance to Slide 3)*

---

### [Slide 3: The Business Problem]
**(1:20 - 2:00 | 40 seconds)**
"So what was our mission? We had to build 'Nutanix Move'—an automated hypervisor migration product. 

The complexity was staggering. We weren't just moving files; we were translating live network topologies and storage architectures across competing platforms with zero margin for error. 

But the real barrier wasn't technical. Despite having top-tier talent, the project immediately hit severe delays. Deadlines slipped by weeks. Integration testing resulted in cascading failures. I needed to find out why."

*(Advance to Slide 4)*

---

### [Slide 4: Four Teams, One Flow]
**(2:00 - 2:30 | 30 seconds)**
"The product workflow crossed through four entirely separate functional pillars.
- The Core Platform team ingested the data.
- The AHV & Networking team deployed the hypervisor.
- Edge Storage committed the data blocks.
- And the UX team created the customer's interface.

Each of these teams was a center of excellence. Individually, they wrote beautiful code. But collectively, the product was entirely broken."

*(Advance to Slide 5)*

---

### [Slide 5: The OrgDNA Framework]
**(2:30 - 2:50 | 20 seconds)**
"To understand why this was happening, I applied the OrgDNA framework from our Organizational Behavior coursework. Specifically, I broke the failure down into three dimensions: Architecture, Culture, and Power & Influence. What I found was a system perfectly designed to produce the delays we were experiencing."

*(Advance to Slide 6)*

---

### [Slide 6: Architecture Analysis]
**(2:50 - 4:00 | 70 seconds)**
"Let’s start with Architecture. Our formal structure was built on deep, functional silos without a shared North Star. 

The absolute root cause of our delays was massive 'structural holes' between the four teams. We did not share a VP. Each team reported up an entirely different chain. To get true alignment on a common goal, decisions technically had to escalate all the way up to the CTO.

Meanwhile, execution was happening four levels down from that. Day-to-day work sat with engineers and managers like myself. But because engineers were incentivized strictly on isolated functional stability, any cross-team interface dispute required a multi-layer escalation: from Engineer, to Manager, to Director, to Senior Director, and finally to VP. This sheer vertical distance meant a technical disagreement that should have taken an hour to resolve added weeks to our timeline. It was a classic 'blind men and the elephant' problem."

*(Advance to Slide 7)*

---

### [Slide 7: Culture Analysis]
**(4:00 - 5:10 | 70 seconds)**
"Next, I looked at our Culture. We had inadvertently fostered an environment of 'Deflection and Blame Shifting.'

Instead of taking joint responsibility, teams actively shifted blame to other functional silos when things failed. A massive avoidance tactic emerged: whenever the Move team highlighted an integration failure, the gatekeeping teams would endlessly demand that we 'reproduce the issue' on our own before they would even look at it. They stalled to delay taking ownership.

Why? Because implicitly, accepting a cross-functional problem damaged your own team's reputation. Deflection wasn't a flaw in our people; it was an ingrained survival habit. As we learned from the NUMMI case, you cannot change culture by telling people to think differently. You have to change what they do every day."

*(Advance to Slide 8)*

---

### [Slide 8: Power & Influence Analysis]
**(5:10 - 6:20 | 70 seconds)**
"Finally, we analyzed Power dynamics. There was a severe imbalance acting as a bottleneck.

The Core Platform and AHV teams held the complex, legacy codebase. They became structural gatekeepers. Meanwhile, the UX and Edge teams had to wait for upstream APIs to be finalized. This created a high degree of asymmetric dependency.

Because the Core engineers had more referential expertise and structural power, upstream delays were often dismissed as 'necessary complexity,' while downstream teams bore the brunt of the schedule slipping. We needed to flatten this power gradient so that downstream teams had voice and visibility without having to beg for API access."

*(Advance to Slide 9)*

---

### [Slide 9: Recommendations (The "Squad" Shift)]
**(6:20 - 7:20 | 60 seconds)**
"So, how did we fix this? We moved beyond the formal organizational chart and completely rewired the DNA. The recommendation was what we called the 'Squad Shift.'

Architecturally, we collapsed the timeline. We overlaid a cross-functional 'broker' role—a Product Manager focused strictly on end-to-end integration flow, not feature sets.

Culturally, we had to shift the norm. We implemented a 'Shared Ownership and Quick Collaboration' mechanism. If an interface blocker emerged, team members could trigger an immediate 30-minute synchronous huddle to resolve it collectively. We normalized early escalation instead of deflection.

And from a Power perspective, we created mutual dependence. We replaced upstream/downstream handoffs with a shared integration backlog, breaking the monopoly of the gatekeeper teams."

*(Advance to Slide 10)*

---

### [Slide 10: Implementation Plan]
**(7:20 - 8:30 | 70 seconds)**
"Implementing this required a phased approach.

Phase 1 is 'Building Awareness & Forming Leadership.' We don't just start with engineers; we start at the top. We build awareness across the organization from the CTO, VPs, and Product Managers to ensure this initiative is explicitly prioritized on every single team's roadmap. Only then do we identify and form the cross-functional leadership squad by pulling leads from each of the four teams.

Phase 2 is 'Shared Visualization.' We built a unified dependency dashboard. For the first time, upstream and downstream blockers were visible on one screen. This replaced implicit power with explicit data.

Phase 3 is 'Institutionalise & Reward.' We revised the incentive structures so that manager performance reviews are strictly tied to cross-functional outcomes, not just local code stability."

*(Advance to Slide 11)*

---

### [Slide 11: Risks & Mitigation]
**(8:30 - 9:00 | 30 seconds)**
"With any structural change, there are risks. 

The highest likelihood risk is resistance from Functional VPs over a perceived loss of autonomy. To mitigate this, we employ 'agenda-linking.' We frame the shared squad model not as a loss of control, but as a protective measure to shield their individual teams from reputation damage and blame-shifting when projects fail."

*(Advance to Slide 12)*

---

### [Slide 12: Success Metrics]
**(9:00 - 9:30 | 30 seconds)**
"We will know this is working by tracking three specific metrics:
1. Operational: A fifty percent reduction in cross-team dependency resolution time.
2. Customer: Net Promoter Scores exceeding 60 due to seamless migration capabilities.
3. Cultural: An increase to 3–5 proactive escalations per sprint—a leading indicator that our engineers finally feel psychologically safe enough to flag problems."

*(Advance to Slide 13)*

---

### [Slide 13: Conclusion]
**(9:30 - 10:00 | 30 seconds)**
"In conclusion, Nutanix's migration project was fundamentally at risk, not because of a failure of technology, but because our DNA was built for functional excellence—not cross-functional delivery.

We had the right talent and the right vision entirely. What was missing was the organizational system designed to let four distinct teams move as one. By restructuring our architecture, reshaping our culture, and balancing power, we can finally capitalize on this once-in-a-decade market window.

Thank you for your time."
