📌 Overview

This project is an offline Python-based tool that automatically extracts key information from supplier quotation PDFs and compiles them into a clean, structured Excel summary sheet.

It is designed to eliminate manual copy-paste work during procurement comparisons while maintaining confidentiality, accuracy, and speed.

📁 What the Tool Does

The script reads all PDFs inside a folder (e.g., /bid/) and extracts:

Supplier Name

Product Name / Item

Quantity

Unit Price (₹)

Total Price (₹)

Delivery Time (Days)

Payment Terms

Warranty/Guarantee

File Name

It generates a single Excel file with one row per supplier quotation.

🛠 Why We Chose an Offline Python Tool
🔐 1. Confidentiality

Quotations contain sensitive pricing, inventory, and supplier details.
Processing them offline ensures that:

No data leaves your computer

No cloud APIs are used

No information is exposed to third parties

This is important for real-world procurement workflows.

📄 2. Structured PDF Advantage

The tool is optimized for quotations with table-like formats, where fields such as:

Supplier Name

Unit Price

Delivery Days

Warranty

appear in a predictable structure.

This allows for accurate and reliable extraction.

⚠️ Project Limitations (Important)

Real-life quotations are not always consistent.

To make the automation accurate, we must understand:

The format of the quotations

Whether numbers appear as text, dropdown/multiple-choice, or handwritten

Whether information is confidential or partially hidden

Whether layouts change between suppliers

📌 If quotations are consistent and structured,

→ Offline Python extraction is 100% reliable.

📌 If quotations are unstructured or formatted differently,

→ Offline scripts may fail or extract incorrect values.
→ In such cases, an AI-based extraction system is needed.

🤖 When and Why AI Is Required

AI becomes necessary when:

Each supplier uses a different template

Tables are missing or inconsistent

Data appears in different locations for different suppliers

Product descriptions vary

Some prices or quantities appear inside paragraphs, not tables

AI can understand context, such as:

“250 per unit” belonging to the correct item
even if the layout changes per quotation.

Offline rule-based methods cannot reliably do this.

📈 Future Improvements

To further improve the automation, we can:

Study actual supplier quotation formats

Detect multiple table formats

Use AI to interpret text contextually

Auto-flag missing or suspicious entries

Support Excel, image-based PDFs, and mixed formats

The more quotation samples we analyze,
the more accurate and intelligent the system becomes.
