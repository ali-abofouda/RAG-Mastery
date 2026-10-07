# 00 - أساسيات ومفاهيم RAG (RAG Fundamentals)

مرحلة تمهيدية تأسيسية مخصصة لشرح وتوثيق فكرة الـ RAG، ودوافع استخدامها، والمقارنة المعيارية مع هندسة الأوامر وإعادة التدريب الدقيق، وصولاً لتفكيك المكونات الهيكلية لمنظومة الـ RAG.

---

## شروحات ومذكرات أساسيات الـ RAG:

1. 📄 **[01 - ما هو الـ RAG؟ (Introduction to RAG)](./01-introduction-to-rag.md)**
   * تعريف الـ RAG وتشبيه الامتحان المفتوح/المغلق (Open vs Closed Book).
   * مشكلات النماذج التقليدية: انقطاع المعرفة والبيانات الخاصة.
   * تفكيك الحروف الثلاثة: Retrieval و Augmentation و Generation.
   * المراحل الثلاث الكبرى لمعمارية الـ RAG.

2. 📄 **[02 - مميزات RAG وأثره في بيئة الأعمال (Advantages & Business Impact)](./02-examples-and-advantages-of-rag.md)**
   * تشبيه الشيف ومكتبة الوصفات ومعضلة الـ Hallucination.
   * مقارنة عملية في خدمة العملاء (Customer Support: Without RAG vs With RAG).
   * دراسات حالة وأرقام دقيقة: JP Morgan ($150M savings)، Microsoft Copilot (94% drop in hallucination)، Bloomberg.
   * الامتثال والحوكمة (100% Source Attribution & Audit Trail)، والعائد الاستثماري (312% ROI).

3. 📄 **[03 - المقارنة الثلاثية: Prompting vs Fine-Tuning vs RAG](./03-prompt-engineering-vs-finetuning-vs-rag.md)**
   * شجرة اتخاذ القرار ومصفوفة المقارنة الشاملة (Decision Tree & Comparison Matrix).
   * تفكيك كل مسار: المفهوم، آلية العمل، الأوزان، والمزايا والعيوب.
   * القاعدة الذهبية للاختيار بين الأساليب الثلاثة.

4. 📄 **[04 - المكونات الأساسية للـ RAG ومرحلة إدخال البيانات (Data Ingestion & Pre-processing)](./04-data-ingestion-and-preprocessing.md)**
   * المكونات الهيكلية الكبرى (Ingestion ➔ Query Processing ➔ Generation).
   * خطوات خط معالجة البيانات: مصادر البيانات المتعددة، التجزئة (Chunking)، وأسبابها.
   * نماذج التضمين الدلالي (Embedding Models: OpenAI & Hugging Face).
   * قواعد البيانات المتجهة (Vector DBs: Chroma, FAISS, Pinecone, DataStax) وتقنيات البحث.

5. 📄 **[05 - معالجة الاستعلام والتوليد (Query Processing & Generation Phases)](./05-query-processing-and-generation.md)**
   * رحلة الاستعلام: تضمين السؤال (Query Embedding)، والبحث الدلالي عن أفضل الفقرات (Top-k Chunks).
   * تعزيز وإثراء السياق بالميتا-داتا وبناء الـ Augmented Prompt.
   * مرحلة التوليد عبر نماذج الـ LLM (OpenAI, Gemini, Llama 3 via Groq).
   * جدول ملخص المعمارية الكاملة والتحضير للانتقال للتطبيق العملي في `01-ingestion`.
