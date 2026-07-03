title: how to use ai and open data to fight misinformation
date: 2026-07-03

When working on integrations of AI and Open Data, we are hitting a bump, as the AI agents keep hallucinating explanations. Even with correct numbers and figures, they can fail by providing the wrong context and making wrong inferences. Let me elaborate.

**First**, AI integrations with Open Data have two sides:

 1. what data owners decide as the interface for their data (APIs, MCPs, Skill Design, etc.),
 2. what data consumers decide to do with it (Prompt, Skills, Workflows, etc.).

<mark>You can make your data available for AI agents, but rarely will you have any say in what they do with it</mark>. This is not new; Open Data has embedded in its definition that what people do with it doesn't have limits (-for any purpose-) and is out of the hands of the data producer. But in the age of AI, this needs to be, at least, revisited.

**And second**, I see two big problems when using AI for analysis and explanations:

 1. It will mostly hallucinate its way out of data gaps,
 2. This gap-filling mechanism will be done either by autocompletion with whatever they "know" (training data) or by answering with whatever strategy they have been programmed to use (they are, at the end of the day, just software).

LLMs accessing the same data can provide different contexts and different interpretations of it. For accurate analysis, <mark>it is not enough to open the data to the AI agent; we must also provide all the information required for its proper use: methodology, boundaries, what can be inferred, what cannot, etc</mark>. For example, an LLM designed to deny climate change or to push a specific agenda can easily ignore all the domain experts' notes and methodology and torture the data to make a claim that experts and publishers will surely not agree on.

Experts in the domain who made the data open should have a say in how AI agents use and interpret the information. The problem, technically speaking, is that the way to do this is via "prompt engineering," which rarely lives in the publisher's information system.

Protocols and Standards for AI should have a way for open data producers to orient and guide the agents consuming it. The MCP protocol has an "instruction" field inside the [initializeResult interface](https://modelcontextprotocol.io/specification/2025-11-25/schema#initializeresult-instructions), but it is optional. In its own definition, it says that it MAY be added to the system prompt, so using it from the client side remains optional. There is no way to properly warn an AI Agent Client that some ways of using the data will result in hallucinations or bad outcomes.

Should AI Interfaces provide more robust mechanisms for it?
