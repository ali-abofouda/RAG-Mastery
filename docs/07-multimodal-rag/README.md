# 07 - الـ RAG متعدد الوسائط (Multimodal RAG)

المرحلة السابعة في مسار إتقان الـ RAG، وتركز على الانتقال الحاسم من التعامل مع النصوص الأحادية (`Unimodal Text`) إلى استيعاب وفهرسة واسترجاع الوثائق الغنية متعددة الوسائط (`Multimodal Documents: Text + Images`)، كالتقارير المالية والرسوم البيانية والمخططات الهندسية المعمارية.

---

## موضوعات شروحات المرحلة:

1. 📄 **[01 - معمارية وأسس الـ Multimodal RAG (Multimodal RAG Architecture & Foundations)](./01-multimodal-rag-architecture.md)**
   * الفجوة المعمارية بين الـ RAG النصي والـ RAG متعدد الوسائط (`Unimodal vs Multimodal`).
   * النماذج اللغوية البصرية (`Multimodal LLMs / Vision-Language Models: GPT-4o, Gemini 2.5 Flash`).
   * فضاء التضمين الموحد ونموذج `CLIP (Contrastive Language-Image Pre-training)`.
   * التدريب التقابلي (`Contrastive Learning`) وتماثل متجهات النصوص والصور.
   * خطوات خط المعالجة الإنتاجي: الاستخراج، التشفير بـ `Base64`، فهرسة `FAISS`، وتنسيق الأوامر البصرية.
   * مصفوفة المفاضلة الهندسية وأسئلة المقابلات المتقدمة.
