# المرحلة 03: فهارس وقواعد بيانات المتجهات (Vector Stores & Databases)
### Comprehensive Architectural Guide (`docs/03-vector-stores-and-databases/`)

المرحلة الثالثة في مسار إتقان الـ RAG، وتتناول الانتقال الحاسم من مجرد إنشاء المتجهات (Embeddings) إلى كيفية حفظها، وفهرستها، وإجراء عمليات البحث والاسترجاع الدلالي السريع عليها باستخدام أدوات التخزين الموضعية وقواعد البيانات السحابية العملاقة.

---

## فهرس موضوعات ومشاريع المرحلة

| الرقم | عنوان الموضوع البرمجي | الشرح المعماري (`docs/`) | الكود المرجعي (`stages/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: |
| 01 | **مقارنة فهارس المتجهات وقواعد بيانات المتجهات** | [01-vector-stores-vs-vector-databases.md](./01-vector-stores-vs-vector-databases.md) | [`01-vector-stores-vs-vector-databases.ipynb`](../../stages/03-vector-stores-and-databases/01-vector-stores-vs-vector-databases/01-vector-stores-vs-vector-databases.ipynb) | مكتمل |
| 02 | **بناء نظام RAG تقليدي باستخدام ChromaDB و LCEL** | [02-traditional-rag-chromadb.md](./02-traditional-rag-chromadb.md) | [`02-traditional-rag-chromadb.ipynb`](../../stages/03-vector-stores-and-databases/02-traditional-rag-chromadb/02-traditional-rag-chromadb.ipynb) | مكتمل |
| 03 | **خوارزميات الفهرسة الحسابية: HNSW و IVF و PQ** | [03-indexing-algorithms-hnsw-ivf-pq.md](./03-indexing-algorithms-hnsw-ivf-pq.md) | [`07-rag-faiss.ipynb`](../../stages/03-vector-stores-and-databases/07-rag-faiss/07-rag-faiss.ipynb) | مكتمل |
| 04 | **الفهرسة عالية الأداء عبر مكتبة FAISS وتسريع الأجهزة** | [04-faiss-high-performance-indexing.md](./04-faiss-high-performance-indexing.md) | [`07-rag-faiss-lcel.ipynb`](../../stages/03-vector-stores-and-databases/07-rag-faiss/07-rag-faiss-lcel.ipynb) | مكتمل |
| 05 | **قواعد البيانات السحابية الموزعة: Pinecone و AstraDB** | [05-cloud-native-databases-pinecone-astradb.md](./05-cloud-native-databases-pinecone-astradb.md) | [`09-astradb-vector-database.ipynb`](../../stages/03-vector-stores-and-databases/09-astradb-vector-database/09-astradb-vector-database.ipynb) & [`10-pinecone.ipynb`](../../stages/03-vector-stores-and-databases/10-pinecone-vector-database/10-pinecone-vector-database.ipynb) | مكتمل |
| 06 | **هندسة فلترة البيانات الوصفية وحوكمة الأمان RBAC** | [06-metadata-filtering-and-security.md](./06-metadata-filtering-and-security.md) | [`04-updating-vector-store.ipynb`](../../stages/03-vector-stores-and-databases/04-updating-vector-store/04-updating-vector-store.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي Senior مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي فني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: مذكرات معمارية وتفصيلية متخصصة ومصاغة وفق أعلى معايير هندسة النظم، متضمنة مخططات Mermaid، صياغات رياضية، ومصفوفات مفاضلة، وأسئلة مقابلات تقنية متقدمة.
