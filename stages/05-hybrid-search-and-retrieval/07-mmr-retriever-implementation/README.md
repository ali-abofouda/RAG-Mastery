# الدرس 07: تطبيق مسترجع أقصى تنوع نسبي (MMR) عملياً
### Practical Implementation of MMR Retrievers (Lecture 47)

يغطي هذا المجلد التطبيق العملي لمسترجع MMR في LangChain وفهارس FAISS:
1. بناء مسترجع بـ `search_type="mmr"`.
2. اختبار وضبط `lambda_mult` و `fetch_k`.
3. قياس التنوع الدلالي ومنع تكرار السياق.
4. دمج المسترجع في مسار LCEL متكامل مع ChatGroq.

* الدفتر المرجعي: [`07-mmr-retriever-implementation.ipynb`](./07-mmr-retriever-implementation.ipynb)
* التوثيق الشامل: [`docs/05-hybrid-search-and-retrieval/07-mmr-retriever-implementation.md`](../../../docs/05-hybrid-search-and-retrieval/07-mmr-retriever-implementation.md)
