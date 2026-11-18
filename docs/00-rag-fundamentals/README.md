# 00 - أساسيات ومفاهيم RAG (RAG Fundamentals)
### Handbook Index & Overview (`docs/00-rag-fundamentals/`)

مرحلة تمهيدية تأسيسية مخصصة لشرح وتوثيق معمارية الـ **RAG**، دوافعها الهندسية، المقارنة المعيارية مع هندسة الأوامر والتدريب الدقيق، وتفكيك خطوط العمل المنفصلة (مسار الـ Ingestion غير المتزامن ومسار الـ Serving المتزامن)، مدعومة **بكود بايثون تطبيقي كامل وقابل للتشغيل**.

---

## فهرس الأدلة المفاهيمية والتطبيقية:

1. 📄 **[01 - ما هو الـ RAG؟ والحدس الهندسي للمعمارية (Introduction to RAG)](./01-introduction-to-rag.md)**
   * مفهوم الـ RAG وتشبيه الامتحان المفتوح والمغلق (Open vs Closed Book).
   * تفكيك الحروف الثلاثة: Retrieval و Augmentation و Generation.
   * المخطط المعماري الشامل (End-to-End Architectural Flow).
   * **الكود التطبيقي**: بناء نظام RAG مصغر وشغال بالكامل من الصفر بالبايثون (`Minimal Working Pipeline`).

2. 📄 **[02 - مميزات RAG وأثره في بيئة الأعمال (Advantages & Business Impact)](./02-examples-and-advantages-of-rag.md)**
   * تشبيه الشيف ومكتبة الوصفات ومعضلة الـ Hallucination.
   * دراسة مقارنة في خدمة العملاء (Customer Support: Without RAG vs With RAG).
   * أرقام ودراسات حالة واقعية من كبرى الشركات (JP Morgan, Microsoft Copilot).
   * حوكمة البيانات، الامتثال (`GDPR / HIPAA`)، وإسناد المصادر (`Source Attribution`).
   * **الكود التطبيقي**: أداة برمجية لفحص صحة الاستشهادات وحساب نسبة الـ Citation Faithfulness.

3. 📄 **[03 - المقارنة الثلاثية: Prompting vs Fine-Tuning vs RAG](./03-prompt-engineering-vs-finetuning-vs-rag.md)**
   * شجرة اتخاذ القرار المعمارية (Decision Tree).
   * تفكيك كل مسار: متى نعدل الأوزان (LoRA) ومتى نسترجع المعرفة ديناميكياً.
   * مصفوفة المقارنة الهندسية الشاملة والمفاضلات (Trade-offs).
   * **الكود التطبيقي**: مقارنة عملية بالبايثون بين استدعاءات المسارات الثلاثة.
   * القاعدة الذهبية للاختيار بين الأساليب.

4. 📄 **[04 - خط إدخال ومعالجة البيانات (Data Ingestion Pipeline)](./04-data-ingestion-and-preprocessing.md)**
   * معمارية الـ Offline Ingestion: Loaders ➔ Splitters ➔ Embedders ➔ Vector DBs.
   * استخراج وتثبيت الميتاداتا لضمان التوثيق وتطبيق الصلاحيات.
   * مفهوم التقطيع النصي والتداخل (`Chunk Size & Overlap`) وأهميته لحفظ السياق.
   * نماذج التضمين الدلالي وقواعد بيانات المتجهات وخوارزميات `ANN`.
   * **الكود التطبيقي**: كلاس تقطيع نصوص ذكي بنمط Sliding Window مع حفظ الميتاداتا وتخزينها في Vector Store.

5. 📄 **[05 - معالجة الاستعلام والتوليد المعزز (Query Processing & Generation)](./05-query-processing-and-generation.md)**
   * مخطط التسلسل الزمني لرحلة الاستعلام اللحظية (`Sequence Diagram`).
   * تضمين الاستعلام وأهمية مطابقة نموذج التضمين.
   * البحث الدلالي مع فلاتر الميتاداتا المسبقة وتطبيق عتبة التشابه (`Similarity Thresholding`).
   * صياغة البرومبت المعزز وفرض قيود منع الهلوسة (`Temperature = 0.0`).
   * **الكود التطبيقي**: كلاس متكامل لخدمة الاستعلامات (`Query Serving Pipeline`) مع الفلترة والرفض التلقائي للأسئلة خارج النطاق.
