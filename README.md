# RAG Mastery

مستودع عملي وهندسي شامل لتوثيق وتطبيق مسار تعلّم أنظمة توليد النصوص المعزز بالاسترجاع (**Retrieval-Augmented Generation - RAG**)، متطابق بالكامل مع منهج ومحتوى الكورس العملي المتقدم (**Ultimate RAG Bootcamp using LangChain, LangGraph, LangSmith**).

> [!TIP]
> **مختبر التجارب الحرة (Interactive Playground Branch)**:  
> لضمان بقاء الفرع الرئيسي (`main`) مرجعاً هندسياً وتعليمياً نقياً ومنظماً، تم تخصيص فرع مستقل لكافة مساحات التجارب الحرة ونوتبوكس الـ Playground:  
> للتبديل وتجربة الأكواد التفاعلية:
> ```bash
> git checkout playground
> ```
> يحتوي فرع `playground` على:
> - `playground/playground.ipynb`: المختبر الشامل لكامل دورة حياة الـ RAG خطوة بخطوة.
> - `playground/01-ingestion/`: مساحات تجارب تفريغ المستندات (PDF, Word, CSV, SQL, JSON).
> - `playground/02-vector-embeddings/`: مساحات تجارب نماذج التضمين السحابية والمفتوحة وتشابه جيب التمام.
> - `playground/03-vector-stores-and-databases/`: مساحات تجارب فهارس وقواعد بيانات المتجهات (FAISS, ChromaDB, إلخ).

---

## 🧭 نظرة عامة على مراحل المسار (Curriculum Breakdown)

| المرحلة | المجلد في المستودع | سكاشن الكورس المقابلة | الوصف وموضوعات المرحلة | الحالة | الدليل والتوثيق |
| :---: | :--- | :---: | :--- | :---: | :---: |
| **00** | **[00-rag-fundamentals](./00-rag-fundamentals/)** | Sections 1–4 (محاضرات 1–8) | أساسيات ومفاهيم RAG، المقارنة مع Fine-tuning، وتجهيز البيئة | [x] | [README.md](./00-rag-fundamentals/README.md) |
| **01** | **[01-ingestion](./01-ingestion/)** | Section 5 (محاضرات 9–18) | تفريغ وتجزئة المستندات بمختلف أنواعها (PDF, Word, CSV, SQL, JSON) | [x] | [README.md](./01-ingestion/README.md) |
| **02** | **[02-vector-embeddings](./02-vector-embeddings/)** | Section 6 (محاضرات 19–23) | نماذج التضمين وفضاء المتجهات والتشابه الدلالي (HuggingFace, OpenAI) | [x] | [README.md](./02-vector-embeddings/README.md) |
| **03** | **[03-vector-stores-and-databases](./03-vector-stores-and-databases/)** | Section 7 (محاضرات 24–36) | فهارس وقواعد بيانات المتجهات (ChromaDB, FAISS, AstraDB, Pinecone, LCEL) | [ ] قيد العمل | [README.md](./03-vector-stores-and-databases/README.md) |
| **04** | **[04-advanced-chunking](./04-advanced-chunking/)** | Section 8 (محاضرات 37–40) | تقنيات التقطيع الدلالي المتقدم (Semantic Chunking with Python & LangChain) | [ ] قادم | [README.md](./04-advanced-chunking/) |
| **05** | **[05-hybrid-search-and-retrieval](./05-hybrid-search-and-retrieval/)** | Section 9 (محاضرات 41–48) | استراتيجيات البحث الهجين (Dense + Sparse), Reranking, و MMR | [ ] قادم | [README.md](./05-hybrid-search-and-retrieval/) |
| **06** | **[06-query-enhancement](./06-query-enhancement/)** | Section 10 (محاضرات 49–52) | تحسين وتوسيع وتفكيك الاستعلامات (Expansion, Decomposition, HyDE) | [ ] قادم | [README.md](./06-query-enhancement/) |
| **07** | **[07-multimodal-rag](./07-multimodal-rag/)** | Section 11 (محاضرات 53–54) | أنظمة RAG متعددة الوسائط للتعامل مع النصوص والصور معاً | [ ] قادم | [README.md](./07-multimodal-rag/) |
| **08** | **[08-langchain-and-langgraph](./08-langchain-and-langgraph/)** | Sections 12–15 (محاضرات 55–89) | إتقان LangChain v1 ومحرك LangGraph وبناء الوكلاء (Agents & Workflows) | [ ] قادم | [README.md](./08-langchain-and-langgraph/) |
| **09** | **[09-agentic-rag](./09-agentic-rag/)** | Sections 16–18 (محاضرات 90–105) | أنظمة Agentic RAG المستقلة، التفكير المتسلسل، والوكلاء المتعددين (Multi-Agents) | [ ] قادم | [README.md](./09-agentic-rag/) |
| **10** | **[10-self-correcting-rag](./10-self-correcting-rag/)** | Sections 19–20 (محاضرات 106–109) | أنماط التصحيح الذاتي المتقدمة (Corrective RAG - CRAG, Adaptive RAG) | [ ] قادم | [README.md](./10-self-correcting-rag/) |
| **11** | **[11-advanced-rag-patterns](./11-advanced-rag-patterns/)** | Sections 21–23 (محاضرات 110–115) | أنماط متقدمة: الذاكرة الدائمة، الـ Cache (CAG)، وأنظمة Vectorless RAG | [ ] قادم | [README.md](./11-advanced-rag-patterns/) |
| **12** | **[12-guardrails-and-gateways](./12-guardrails-and-gateways/)** | Sections 24–25 (محاضرات 116–117) | تأمين النظام وبوابات النماذج اللغوية (Guardrails & LLM Gateways) | [ ] قادم | [README.md](./12-guardrails-and-gateways/) |
| **13** | **[13-evaluation](./13-evaluation/)** | Section 26 (محاضرات 118–122) | تقييم دقة وجودة الـ Chatbot وأنظمة RAG باستخدام LLM-as-a-judge والمقاييس المعيارية | [ ] قادم | [README.md](./13-evaluation/) |
| **14** | **[14-knowledge-graphs](./14-knowledge-graphs/)** | Sections 27–28 (محاضرات 123–133) | الرسوم البيانية المعرفية، لغة Cypher، وقواعد Neo4j مع GraphRAG | [ ] قادم | [README.md](./14-knowledge-graphs/) |
| **15** | **[capstone](./capstone/)** | Sections 29–30 (محاضرات 134–142) | المشروع الختامي المتكامل (End-to-End RAG Search Application & RolePlay) | [ ] قادم | [README.md](./capstone/) |

---

## 🗂️ الموارد المشتركة

* **[course content/](./course%20content/)**: الفهرس الشامل والتفصيلي لمحتوى الكورس (`content.md`).
* **[data/](./data/)**: مجلد البيانات المعيارية المشتركة (PDF, Word, CSV, SQL, JSON, TXT).
* **[articles/](./articles/)**: مقالات ملخصة، مراجع تقنية، وأوراق بحثية مهمة حول RAG.
* **[notes/](./notes/)**: مساحة الملاحظات والملخصات المفاهيمية العامة.
