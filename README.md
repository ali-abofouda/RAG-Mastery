# RAG Mastery

مستودع عملي وهندسي شامل لتوثيق وتطبيق مسار تعلّم أنظمة توليد النصوص المعزز بالاسترجاع (**Retrieval-Augmented Generation - RAG**)، متطابق بالكامل مع منهج ومحتوى الكورس العملي المتقدم (**Ultimate RAG Bootcamp using LangChain, LangGraph, LangSmith**).

---

## 🏛️ معمارية المستودع الثلاثية (The 3-Pillar Repository Architecture)

ينتظم المشروع في **3 مجلدات رئيسية واضحة ومستقلة** لتفادي التشتت وفصل الشرح النظري والمعماري عن الكود النموذجي ومعمل التجارب:

1. **[`docs/`](./docs/) — الشرح النظري والمعماري الشامل**:
   * المفاهيم الهندسية والنظرية المشروحة خطوة بخطوة.
   * المخططات المعمارية ومسارات التدفق (`Mermaid Diagrams`).
   * التحليلات والمعادلات الرياضية.
   * المقارنات والـ `Trade-offs` لبيئات الإنتاج.

2. **[`stages/`](./stages/) — الكود النموذجي المرجعي المكتمل**:
   * الكود البرمجي الكامل والنموذجي المنفذ مسبقاً بمخرجاته الحقيقية (`Production Reference Code`).
   * خلايا برمجية متسلسلة بتعليقات توضيحية احترافية بالإنجليزية (`Inline Comments`).
   * خالي تماماً من الإيموجي ومختبر بالكامل عبر `Assertions`.

3. **[`playground/`](./playground/) — معمل التجارب والتطبيق العملي**:
   * مساحات تفاعلية مخصصة للمتدرب لكتابة وتجربة الأكواد بنفسه.
   * مساحات تجارب حرة لاختبار نصوص واستعلامات مخصصة (`Hands-on Lab`).

---

## 🧭 نظرة عامة على مراحل المسار (Curriculum Breakdown)

| المرحلة | الشرح النظري (`docs/`) | الكود النموذجي (`stages/`) | معمل التجارب (`playground/`) | سكاشن الكورس | موضوعات المرحلة | الحالة |
| :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **00** | [README](./docs/00-rag-fundamentals/README.md) | [Notebook](./stages/00-rag-fundamentals/) | — | Sections 1–4 | أساسيات ومفاهيم RAG وتجهيز البيئة | [x] |
| **01** | [README](./docs/01-ingestion/README.md) | [Notebooks](./stages/01-ingestion/) | [Lab](./playground/01-ingestion/) | Section 5 | تفريغ وتجزئة المستندات (PDF, Word, CSV, SQL, JSON) | [x] |
| **02** | [README](./docs/02-vector-embeddings/README.md) | [Notebooks](./stages/02-vector-embeddings/) | [Lab](./playground/02-vector-embeddings/) | Section 6 | نماذج التضمين وفضاء المتجهات والتشابه الدلالي | [x] |
| **03** | [README](./docs/03-vector-stores-and-databases/README.md) | [Notebooks](./stages/03-vector-stores-and-databases/) | [Lab](./playground/03-vector-stores-and-databases/) | Section 7 | فهارس وقواعد بيانات المتجهات (Chroma, FAISS, AstraDB, Pinecone) | [x] مكتمل |
| **04** | [README](./docs/04-advanced-chunking/README.md) | [Notebooks](./stages/04-advanced-chunking/) | [Lab](./playground/04-advanced-chunking/) | Section 8 | تقنيات التقطيع الدلالي المتقدم (Semantic Chunking) | [x] مكتمل |
| **05** | — | 05-hybrid-search | — | Section 9 | استراتيجيات البحث الهجين (Dense + Sparse) و Reranking | [ ] قادم |
| **06** | — | 06-query-enhancement | — | Section 10 | تحسين وتوسيع وتفكيك الاستعلامات (Expansion, HyDE) | [ ] قادم |
| **07** | — | 07-multimodal-rag | — | Section 11 | أنظمة RAG متعددة الوسائط للنصوص والصور | [ ] قادم |
| **08** | — | 08-langchain-and-langgraph | — | Sections 12–15 | إتقان LangChain v1 و LangGraph وبناء الوكلاء | [ ] قادم |
| **09** | — | 09-agentic-rag | — | Sections 16–18 | أنظمة Agentic RAG المستقلة والوكلاء المتعددين | [ ] قادم |
| **10** | — | 10-self-correcting-rag | — | Sections 19–20 | أنماط التصحيح الذاتي (Corrective RAG - CRAG) | [ ] قادم |
| **11** | — | 11-advanced-rag-patterns | — | Sections 21–23 | الذاكرة الدائمة، الـ Cache (CAG)، وأنظمة Vectorless RAG | [ ] قادم |
| **12** | — | 12-guardrails-and-gateways | — | Sections 24–25 | تأمين النظام وبوابات النماذج اللغوية (Guardrails) | [ ] قادم |
| **13** | — | 13-evaluation | — | Section 26 | تقييم دقة وجودة الـ RAG عبر مقاييس RAGAS المعيارية | [ ] قادم |
| **14** | — | 14-knowledge-graphs | — | Sections 27–28 | الرسوم البيانية المعرفية وقواعد Neo4j مع GraphRAG | [ ] قادم |
| **15** | [README](./docs/capstone/README.md) | [Capstone](./stages/capstone/) | — | Sections 29–30 | المشروع الختامي المتكامل (End-to-End Application) | [ ] قادم |

---

## 🗂️ الموارد المشتركة

* **[course content/](./course%20content/)**: الفهرس الشامل والتفصيلي لمحتوى الكورس (`content.md`).
* **[data/](./data/)**: مجلد البيانات المعيارية المشتركة (PDF, Word, CSV, SQL, JSON, TXT).
* **[articles/](./articles/)**: مقالات ملخصة، مراجع تقنية، وأوراق بحثية مهمة حول RAG.
* **[notes/](./notes/)**: مساحة الملاحظات والملخصات المفاهيمية العامة.
