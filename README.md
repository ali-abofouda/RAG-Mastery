# RAG Mastery: الدليل الهندسي المتكامل لأنظمة توليد النصوص المعزز بالاسترجاع

مستودع عملي وهندسي شامل لتوثيق وتطبيق مسار تعلم أنظمة توليد النصوص المعززة بالاسترجاع (**Retrieval-Augmented Generation - RAG**)، متطابق بالكامل مع منهج ومحتوى الكورس العملي المتقدم (**Ultimate RAG Bootcamp using LangChain, LangGraph, LangSmith**).

> **حجم المسار المحدث:** 32 سكشن • 191 محاضرة عملية • 45 ساعة تدريبية وتطبيقية متكاملة.  
> **الدليل المعماري للمشاريع الإنتاجية والـ AI FDE:** متوفر في [`notes/ENTERPRISE_MODULES_DEEP_DIVE.md`](./notes/ENTERPRISE_MODULES_DEEP_DIVE.md).

---

## معمارية المستودع الثلاثية (The 3-Pillar Repository Architecture)

ينتظم المشروع في **3 ركائز رئيسية واضحة ومستقلة** لتفادي التشتت وفصل الشرح النظري والمعماري عن الكود النموذجي ومعمل التجارب:

1. **[`docs/`](./docs/) — الشرح النظري والمعماري الشامل**:
   * المفاهيم الهندسية والنظرية المشروحة خطوة بخطوة باللغة العربية مع مصطلحات تقنية دقيقة.
   * المخططات المعمارية ومسارات التدفق (`Mermaid Diagrams`).
   * التحليلات والمعادلات الرياضية بصيغة KaTeX.
   * المقارنات الهندسية ودراسة المفاضلات (`Trade-offs`) لبيئات الإنتاج.

2. **[`stages/`](./stages/) — الكود المرجعي المعتمد للإنتاج (Production Reference Code)**:
   * كود برمجي كامل، منظم، ومسبق التنفيذ بمخرجاته الحقيقية، ومقسم إلى مجلدات فرعية لكل محاضرة مع توثيق معماري مستقل.
   * تعليقات إنجليزية تقنية بحتة تشرح المنطق البرمجي بالتفصيل (`Inline English Comments`).
   * خالٍ تماماً من الرموز التعبيرية ومختبر بالكامل عبر فحوصات التأكيد الصارمة (`Assertions`).

3. **[`playground/`](./playground/) — كشكول التجارب التفاعلي الودود (Interactive Learning Lab)**:
   * مكتوب بأسلوب بشري بسيط ومريح لإنسان يتعلم ويجرب بنفسه خطوة بخطوة.
   * خلايا برمجية قصيرة ومركزة تدعم التجربة الفورية والتعديل الحر دون قيود أو تعقيدات.
   * مساحات حرة لاختبار الاستعلامات وتغيير المعاملات والأوزان وملاحظة النتائج عملياً.

---

## 🌐 بوابة القراءة والتعلم التفاعلية (Learning Portal)

لقراءة وتصفح محتوى المنهج والدروس النظرية (`docs/`) في واجهة ويب حديثة وسريعة ومصممة خصيصاً للقراءة المريحة (خط عربي تقني، دعم المعادلات الرياضية KaTeX ومخططات المعمارية Mermaid، الوضع الليلي، والبحث الفوري):

```bash
# تشغيل البوابة وفتحها تلقائياً في المتصفح
python run_portal.py
```

---

## جدول تقدم موضوعات المسار (Curriculum Breakdown)

| المرحلة | الشرح النظري (`docs/`) | الكود المرجعي (`stages/`) | معمل التجارب (`playground/`) | سكاشن الكورس | موضوعات المرحلة الأساسية | الحالة |
| :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **00** | [README](./docs/00-rag-fundamentals/README.md) | [Notebook](./stages/00-rag-fundamentals/) | — | Sections 1–4 | أساسيات ومفاهيم RAG وإعداد البيئة البرمجية | [x] مكتمل |
| **01** | [README](./docs/01-ingestion/README.md) | [Notebooks](./stages/01-ingestion/) | [Lab](./playground/01-ingestion/) | Section 5 | استخراج ومعالجة المستندات (PDF, Word, CSV, SQL, JSON) | [x] مكتمل |
| **02** | [README](./docs/02-vector-embeddings/README.md) | [Notebooks](./stages/02-vector-embeddings/) | [Lab](./playground/02-vector-embeddings/) | Section 6 | نماذج التضمين وفضاء المتجهات والتشابه الدلالي | [x] مكتمل |
| **03** | [README](./docs/03-vector-stores-and-databases/README.md) | [Notebooks](./stages/03-vector-stores-and-databases/) | [Lab](./playground/03-vector-stores-and-databases/) | Section 7 | قواعد بيانات الفيكتورز (Chroma, FAISS, AstraDB, Pinecone) | [x] مكتمل |
| **04** | [README](./docs/04-advanced-chunking/README.md) | [Notebooks](./stages/04-advanced-chunking/) | [Lab](./playground/04-advanced-chunking/) | Section 8 | تقنيات التقطيع الدلالي المتقدم (Semantic Chunking) | [x] مكتمل |
| **05** | [README](./docs/05-hybrid-search-and-retrieval/README.md) | [Notebooks](./stages/05-hybrid-search-and-retrieval/) | [Lab](./playground/05-hybrid-search-and-retrieval/) | Section 9 | استراتيجيات البحث الهجين (Dense + BM25) وإعادة الترتيب Reranking وخوارزمية MMR | [x] مكتمل (المحاضرات 41–48) |
| **06** | — | 06-query-enhancement | — | Section 10 | تحسين وتوسيع وتفكيك الاستعلامات (Expansion, HyDE) | [ ] قادم |
| **07** | — | 07-multimodal-rag | — | Section 11 | أنظمة RAG متعددة الوسائط للنصوص والصور | [ ] قادم |
| **08** | — | 08-langchain-and-langgraph | — | Sections 12–15 | تحديثات LangChain v1 و LangGraph وبناء الوكلاء | [ ] قادم |
| **09** | — | 09-agentic-rag | — | Sections 16–18 | أنظمة Agentic RAG المستقلة والوكلاء المتعددين | [ ] قادم |
| **10** | — | 10-self-correcting-rag | — | Sections 19–20 | أنماط التصحيح الذاتي (Corrective RAG - CRAG, Adaptive RAG) | [ ] قادم |
| **11** | — | 11-advanced-rag-patterns | — | Sections 21–23 | الذاكرة الدائمة، الـ Cache (CAG)، وأنظمة Vectorless RAG | [ ] قادم |
| **12** | — | 12-guardrails-and-gateways | — | Sections 24–25 | تأمين النظم وبوابات النماذج اللغوية (Guardrails & LLM Gateways) | [ ] قادم |
| **13** | — | 13-evaluation | — | Section 26 | تقييم دقة وجودة الـ RAG عبر مقاييس LLM-as-a-judge | [ ] قادم |
| **14** | — | 14-knowledge-graphs | — | Sections 27–28 | الرسوم البيانية المعرفية وقواعد Neo4j مع GraphRAG | [ ] قادم |
| **15** | [README](./docs/capstone/README.md) | [Capstone](./stages/capstone/) | — | Section 29 | المشروع المتكامل: تطبيق ويب مع React Agent و Wikipedia و Streamlit | [ ] قادم |
| **16** | — | 16-enterprise-hr-rag | — | Section 30 | مشروع الشركات: HR Policy RAG Assistant (Full Stack, Security & Docker) | [ ] قادم |
| **17** | — | 17-ecommerce-ai-fde | — | Sections 31–32 | محاكاة مهندس الذكاء الاصطناعي الميداني (AI FDE Roleplay on GCP) | [ ] قادم |

---

## الموارد المشتركة والملفات المرجعية

* **[`course content/`](./course%20content/)**: الفهرس الشامل والتفصيلي لمحتوى الكورس بـ 32 سكشن و 191 محاضرة (`content.md`).
* **[`notes/`](./notes/)**: مساحة الملاحظات، خطة المذاكرة المكثفة، والدليل المعماري لمشاريع الإنتاج المتقدمة (`ENTERPRISE_MODULES_DEEP_DIVE.md`).
* **[`data/`](./data/)**: مجلد البيانات المعيارية المشتركة (PDF, Word, CSV, SQL, JSON, TXT).
* **[`articles/`](./articles/)**: مقالات ملخصة، مراجع تقنية، وأوراق بحثية حول معمارية الـ RAG.

---

## معايير الجودة المعتمدة
- **سلامة الترميز الدولي**: جميع الملفات محفوطة بترميز `UTF-8` الصارم لضمان القراءة السليمة للغة العربية والمصطلحات الإنجليزية.
- **BiDi Safety**: جميع المصطلحات الإنجليزية والمعرفات البرمجية محاطة بعلامات الاقتباس المائلة (`` `code` ``).
- **Zero Emojis in Stages**: كود الإنتاج في مجلد `stages` خالٍ تماماً من الإيموجي في التعليقات أو المخرجات لضمان الاحترافية البرمجية.
