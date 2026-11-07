# الدرس 05: التطبيق العملي لإعادة الترتيب (Reranking Implementation)
### Practical Implementation with LLM-as-a-Reranker (Lecture 45)

يغطي هذا المجلد التطبيق العملي لإعادة الترتيب كما ورد في المحاضرة 45:
1. تحميل وتقطيع ملف `langchain_sample.txt`.
2. الاسترجاع الأولي السريع عبر فهرس FAISS في الذاكرة.
3. بناء برومبت إعادة الترتيب بالنموذج اللغوي (`ChatGroq`).
4. تحليل الأرقام الفاصلة وإعادة ترتيب الوثائق برمجياً لرفع دقة السياق.

* الدفتر المرجعي: [`05-reranking-implementation.ipynb`](./05-reranking-implementation.ipynb)
* التوثيق الشامل: [`docs/05-hybrid-search-and-retrieval/05-reranking-implementation.md`](../../../docs/05-hybrid-search-and-retrieval/05-reranking-implementation.md)
