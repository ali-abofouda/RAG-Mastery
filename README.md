# RAG Mastery

مستودع عملي لتوثيق وتطبيق مسار تعلّم أنظمة توليد النصوص المعزز بالاسترجاع (Retrieval-Augmented Generation - RAG)، يغطي المراحل من الأساسيات النظرية حتى الأنظمة المتقدمة والجاهزية للإنتاج.

## نظرة عامة على المراحل

يمر المسار بـ 12 مرحلة متكاملة:
0. **00-rag-fundamentals**: شرح فكرة وأساسيات RAG، المزايا، أثر حالات الاستخدام، المقارنة الثلاثية، وتفكيك المعمارية.
1. **01-ingestion**: استيراد وتجزئة وتحليل مختلف أنواع البيانات والمستندات (PDF/Word/CSV/SQL).
2. **02-indexing**: تحويل النصوص لتمثيلات شعاعية وفهرستها مع إثراء البيانات الوصفية (Embeddings, Vector Stores, Metadata Enrichment).
3. **03-retrieval**: البحث عن المعلومات الأكثر صلة بالاستعلام باستخدام تقنيات مطابقة وإعادة ترتيب متعددة (Similarity, Hybrid, MMR, Reranking).
4. **04-query-understanding**: تحسين وتفكيك وتوسيع وتوجيه الاستعلامات (Expansion, Decomposition, HyDE, Query Routing).
5. **05-generation**: تركيب وتوليد الإجابات باستخدام السياق المسترجع وسلاسل التنفيذ وإدارة الذاكرة (LCEL, Conversational Memory).
6. **06-agentic-rag**: بناء وكلاء أذكياء لاتخاذ قرارات الاسترجاع واستخدام الأدوات بشكل مستقل (ReAct, Tool Use, Multi-agent).
7. **07-self-correcting-rag**: تطبيق أنماط التقييم الذاتي والتصحيح التلقائي للاسترجاع والإجابات (CRAG, Self-RAG, Adaptive RAG).
8. **08-knowledge-graphs**: استرجاع البيانات المترابطة وعلاقاتها باستخدام الرسوم البيانية المعرفية (Neo4j, Cypher, Graph RAG).
9. **09-evaluation**: قياس وتقييم دقة وجودة مخرجات النظام بمقاييس معيارية (RAGAS, LLM-as-judge).
10. **10-production-readiness**: تأمين وحماية ومراقبة النظام وضبط التكلفة وزمن الاستجابة للإنتاج (Guardrails, LLM Gateway, Latency & Cost).
11. **capstone**: تطبيق متكامل يتيح رفع المستندات والتفاعل معها (واجهة أمامية، خلفية، وحاويات Docker).

---

## الموارد الإضافية

* **[articles/](./articles/)**: مقالات ملخصة، مراجع تقنية، وأوراق بحثية مهمة حول RAG.
* **[notes/](./notes/)**: مساحة الملاحظات والملخصات المفاهيمية العامة.

---

## جدول التقدّم

| المرحلة | الوصف | الحالة | الملاحظات | الـ Playground المنظم |
| :--- | :--- | :---: | :---: | :---: |
| [00-rag-fundamentals](./00-rag-fundamentals/) | أساسيات ومفاهيم وشرح فكرة RAG | [ ] | [notes](./00-rag-fundamentals/) | - |
| [01-ingestion](./01-ingestion/) | معالجة وإدخال البيانات | [ ] | [notes](./notes/) | - |
| [02-indexing](./02-indexing/) | التضمينات وفهارس المتجهات | [ ] | [notes](./notes/) | - |
| [03-retrieval](./03-retrieval/) | الاسترجاع وإعادة الترتيب | [ ] | [notes](./notes/) | - |
| [04-query-understanding](./04-query-understanding/) | فهم وتحسين الاستعلامات | [ ] | [notes](./notes/) | - |
| [05-generation](./05-generation/) | توليد الإجابات وسلاسل LCEL | [ ] | [notes](./notes/) | - |
| [06-agentic-rag](./06-agentic-rag/) | وكلاء RAG واتخاذ القرار | [ ] | [notes](./notes/) | - |
| [07-self-correcting-rag](./07-self-correcting-rag/) | أنماط RAG المصححة ذاتياً | [ ] | [notes](./notes/) | - |
| [08-knowledge-graphs](./08-knowledge-graphs/) | الرسوم البيانية المعرفية | [ ] | [notes](./notes/) | - |
| [09-evaluation](./09-evaluation/) | التقييم ومقاييس الأداء | [ ] | [notes](./notes/) | - |
| [10-production-readiness](./10-production-readiness/) | الحماية والمراقبة والإنتاج | [ ] | [notes](./notes/) | - |
| [capstone](./capstone/) | المشروع الختامي المتكامل | [ ] | - | - |
