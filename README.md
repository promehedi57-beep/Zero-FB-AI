# 🌐 Zero IP Rotator | Zero FB AI Edition 🔄

**Zero IP Rotator** হলো একটি পাওয়ারফুল অটোমেটিক আইপি চেঞ্জার টুল। এটি বিশেষভাবে **Termux** এবং **Linux** ব্যবহারকারীদের জন্য তৈরি করা হয়েছে যারা **Zero Number Bot** বা **Zero FB AI** নিয়ে কাজ করেন এবং যাদের ঘনঘন আইপি পরিবর্তন করা প্রয়োজন।

![Termux](https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=termux&logoColor=white)
![Tor](https://img.shields.io/badge/Tor-7D4698?style=for-the-badge&logo=tor-project&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🚀 বৈশিষ্ট্যসমূহ (Features)

* **অটোমেটিক আইপি রোটেশন:** নির্দিষ্ট সময় পর পর আপনার আইপি নিজে থেকেই বদলে যাবে।
* **মাল্টি-টর সাপোর্ট:** একসাথে ৫টি টর ইনস্ট্যান্স চলে, যা কানেকশনকে আরও ফাস্ট করে।
* **জিরো স্টাইল ইন্টারফেস:** সুন্দর ASCII আর্ট এবং রঙিন ইউজার ইন্টারফেস।
* **সহজ কমান্ড:** খুব সহজেই রোটেশন টাইম সেট করা যায়।

---

## 🛠 ইনস্টলেশন পদ্ধতি (Installation Methods)

আপনার পছন্দমতো যেকোনো একটি পদ্ধতিতে এটি সেটআপ করতে পারেন:

### ১. গিট ক্লোন পদ্ধতি (Git Clone Method)
সবচেয়ে নিরাপদ এবং আপডেট পদ্ধতি:

```bash
pkg update && pkg upgrade -y
pkg install git tor curl netcat-openbsd -y
git clone [https://github.com/promehedi57/Zero-FB-AI.git](https://github.com/promehedi57/Zero-FB-AI.git)
cd Zero-FB-AI
chmod +x zero-ip.sh
./zero-ip.sh
