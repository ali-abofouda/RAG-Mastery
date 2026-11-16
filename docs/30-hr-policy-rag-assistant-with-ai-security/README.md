# القسم 30: مشروع مساعد سياسات الموارد البشرية المؤمن للشركات (Section 30: HR Policy RAG Assistant with AI Security)

مرحباً بك في توثيق **القسم الثلاثين (Section 30)** وهو **المشروع التطبيقي الأول للشركات الكبرى** ضمن مسار **RAG-Mastery**. يركز هذا المشروع المتقدم على بناء وتشغيل ونشر نظام استرجاع وتوليد متكامل مخصص لقطاع الموارد البشرية في المؤسسات، ومحصن بأعلى معايير الأمان ضد الهجمات السيبرانية وكسر الحماية (`Jailbreaks & Red Teaming`).

---

## خريطة وثائق ومحاضرات المشروع (Project Lectures Roadmap)

| رقم المحاضرة | عنوان المحاضرة | الوثيقة المعمارية (`docs/`) | الكود المرجعي والتطبيقي (`projects/`) | المرحلة (Phase) |
| :---: | :--- | :--- | :--- | :---: |
| **142** | الترحيب بمشروع مساعد الـ HR واستعراض النظام الحي | [`01-hr-policy-assistant-architecture-and-overview.md`](./01-hr-policy-assistant-architecture-and-overview.md) | [`projects/01-rag-applications/01-hr-policy-rag-assistant/`](../../projects/01-rag-applications/01-hr-policy-rag-assistant/) | Kickoff & Overview (مكتمل) |
| **143** | مقدمة لمعمارية المشروع ومراحل التطور الثلاث | [`02-project-architecture-and-three-phase-evolution.md`](./02-project-architecture-and-three-phase-evolution.md) | [`projects/01-rag-applications/01-hr-policy-rag-assistant/`](../../projects/01-rag-applications/01-hr-policy-rag-assistant/) | Architecture & Roadmap (مكتمل) |
| **144** | الطور الأول: تأسيس الاسترجاع الهجين المحلي وهندسة البيانات المشوشة | [`03-phase-1-local-hybrid-rag-foundations.md`](./03-phase-1-local-hybrid-rag-foundations.md) | [`projects/01-rag-applications/01-hr-policy-rag-assistant/`](../../projects/01-rag-applications/01-hr-policy-rag-assistant/) | Phase 1: Foundations & Setup (مكتمل) |
| **145** | إدارة الإعدادات المركزية وتكوين البيئة والمفاتيح | [`04-project-settings-and-configuration-management.md`](./04-project-settings-and-configuration-management.md) | [`projects/01-rag-applications/01-hr-policy-rag-assistant/`](../../projects/01-rag-applications/01-hr-policy-rag-assistant/) | Phase 1: Configuration Management (مكتمل) |
| **146** | تحميل الوثائق وهندسة معالجة الصيغ المتعددة وموجهات النظام | [`05-document-loading-and-multi-format-processing.md`](./05-document-loading-and-multi-format-processing.md) | [`projects/01-rag-applications/01-hr-policy-rag-assistant/`](../../projects/01-rag-applications/01-hr-policy-rag-assistant/) | Phase 1: Document Loading & Multi-format (مكتمل) |
| **147** | تقطيع المستندات وتوليد التضمينات والتخزين المتجهي الهجين | [`06-document-chunking-and-vector-store-ingestion.md`](./06-document-chunking-and-vector-store-ingestion.md) | [`projects/01-rag-applications/01-hr-policy-rag-assistant/`](../../projects/01-rag-applications/01-hr-policy-rag-assistant/) | Phase 1: Ingestion & Hybrid Vector Store (مكتمل) |
| **148 - 151** | بناء خط أنابيب الإدخال والاسترجاع وإعادة الترتيب | قيد المعالجة | قيد المعالجة | Phase 1: Ingestion & Retrieval Pipeline |
| **152 - 159** | الطور الثاني: أمان النماذج اللغوية واختبارات الاختراق | قيد المعالجة | قيد المعالجة | Phase 2: LLM Security & Evals |
| **160 - 163** | الطور الثالث: الحاويات والنشر السحابي الكامل | قيد المعالجة | قيد المعالجة | Phase 3: Deployment |

---

## الأهداف المعمارية والعملية للمشروع
1. **التعامل مع قواعد البيانات المشوشة (`Noisy Enterprise Databases`)** عبر تقنيات الـ `Re-ranking` لضمان دقة الاسترجاع حتى في بيئات البيانات غير المنتظمة.
2. **بناء بوابة ذكاء اصطناعي ذاتية الاستضافة (`Self-Hosted LiteLLM Gateway`)** لتوحيد الاستدعاء وإدارة التبديل التلقائي بين النماذج وحساب التكاليف.
3. **تطبيق دروع الحماية المتقدمة (`Google Model Armor & Guardrails`)** لمنع الـ Prompt Injection وتحديد نطاق التخصص.
4. **توفير كاش دلالي ذكي (`Semantic Caching`)** لتخفيض زمن الاستجابة إلى الصفر وتوفير تكاليف استدعاء النماذج.
5. **إجراء اختبارات الفريق الأحمر (`Red Teaming`)** للتحقق البرمجي من مناعة النظام ضد هجمات كسر الشخصية وتجاوز التعليمات.
6. **النشر السحابي الإنتاجي (`Cloud-Native Deployment`)** باستخدام Docker و Google Cloud Run وحماية الدخول عبر Google OAuth.
