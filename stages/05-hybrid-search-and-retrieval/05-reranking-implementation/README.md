# الدرس 05: التطبيق العملي لخوارزميات إعادة الترتيب (Reranking Implementation)
### Practical Implementation with Cross-Encoders and FlashRank (Lecture 45)

يغطي هذا المجلد التطبيق البرمجي الشامل للمحاضرة 45 من كورس RAG Mastery، حيث نطبق إعادة الترتيب عبر:
1. بناء مسترجع أولي يستخرج أفضل 10 مرشحين باستخدام التضمينات الكثيفة (`FAISS`).
2. إعادة ترتيب الوثائق باستخدام نموذج `CrossEncoder` الكلاسيكي (`cross-encoder/ms-marco-MiniLM-L-6-v2`).
3. إعادة الترتيب باستخدام مكتبة `FlashRank` الخفيفة المسرعة بـ ONNX.
4. دمج إعادة الترتيب في خط إنتاج RAG متكامل عبر `ContextualCompressionRetriever` وربطه مع نموذج `ChatGroq`.

---

## الملفات الملحقة
* [`05-reranking-implementation.ipynb`](./05-reranking-implementation.ipynb): الدفتر المرجعي الهندسي المكتوب بالإنجليزية وفق معايير Senior AI Engineer مع اختبارات تحقق دقيقة ومخرجات تشغيل محفوظة.
* التوثيق النظري والمعماري: [`docs/05-hybrid-search-and-retrieval/05-reranking-implementation.md`](../../../docs/05-hybrid-search-and-retrieval/05-reranking-implementation.md)
