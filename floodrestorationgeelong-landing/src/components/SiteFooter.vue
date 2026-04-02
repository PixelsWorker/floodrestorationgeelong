<template>
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <img 
          src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Logo-1-removebg-preview-300x133.jpg" 
          alt="Flood Restoration Geelong Logo"
          class="footer-logo"
        />
        <p>Your local Geelong experts in emergency flood recovery and water damage repairs. Available 24/7 for residential and commercial properties.</p>
        <div class="social-links">
          <a href="#" aria-label="Facebook">FB</a>
          <a href="#" aria-label="Instagram">IG</a>
          <a href="#" aria-label="YouTube">YT</a>
          <a href="#" aria-label="TikTok">TK</a>
        </div>
      </div>

      <div class="footer-links">
        <h3>Quick Links</h3>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About Us</a></li>
          <li><a href="/faqs">Faq's</a></li>
          <li><a href="/blogs">Blog's</a></li>
          <li><a href="/area-we-service">Area We Service</a></li>
        </ul>
      </div>

      <div class="footer-services">
        <h3>Our Services</h3>
        <ul>
          <li><a href="/emergency-water-restoration-geelong">Emergency Restoration</a></li>
          <li><a href="/carpet-water-extraction-geelong">Carpet Extraction</a></li>
          <li><a href="/mould-remediation-geelong">Mould Remediation</a></li>
          <li><a href="/burst-pipes-geelong">Burst Pipes</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">
        <p>&copy; 2026 Flood Restoration Geelong | All rights reserved. | Design By <a href="https://chinedigital.com.au/" target="_blank">CHINE DIGITAL</a></p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  background-color: var(--secondary-color);
  color: var(--white);
  padding: 80px 0 0;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 60px;
  margin-bottom: 60px;
}

.footer-logo {
  height: 80px;
  margin-bottom: 20px;
  filter: brightness(0) invert(1);
}

.footer-brand p {
  opacity: 0.7;
  font-size: 15px;
  line-height: 1.8;
  margin-bottom: 25px;
}

.social-links {
  display: flex;
  gap: 15px;
}

.social-links a {
  width: 40px;
  height: 40px;
  background-color: rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-weight: 700;
  font-size: 12px;
}

.social-links a:hover {
  background-color: var(--primary-color);
}

h3 {
  font-size: 18px;
  margin-bottom: 25px;
  position: relative;
  padding-bottom: 10px;
}

h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 30px;
  height: 2px;
  background-color: var(--primary-color);
}

ul li {
  margin-bottom: 12px;
}

ul li a {
  opacity: 0.7;
  font-size: 15px;
}

ul li a:hover {
  opacity: 1;
  color: var(--primary-color);
  padding-left: 5px;
}

.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.1);
  padding: 25px 0;
  text-align: center;
  font-size: 14px;
}

.footer-bottom p {
  opacity: 0.5;
}

.footer-bottom a {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
</style>
