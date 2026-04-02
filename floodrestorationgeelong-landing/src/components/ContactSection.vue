<template>
  <section class="contact" id="contact">
    <div class="container narrow">
      <div class="contact-box">
        <div class="contact-info">
          <h2>Contact Us</h2>
          <p>Available 24/7 for emergency flood and water damage response. We’re here to help when you need us most.</p>
          
          <div class="info-item">
            <span class="icon">📞</span>
            <div>
              <strong>Phone</strong>
              <p><a href="tel:0459338998">0459 338 998</a></p>
            </div>
          </div>
          
          <div class="info-item">
            <span class="icon">📧</span>
            <div>
              <strong>Email</strong>
              <p><a href="mailto:info@floodrestorationgeelong.au">info@floodrestorationgeelong.au</a></p>
            </div>
          </div>
        </div>

        <div class="contact-cta">
          <div class="cta-card">
            <h3>Get a Professional Quote</h3>
            <p>Our experts are standing by. Click below to reach our main contact portal and request a free, no-obligation quote today.</p>
            <a 
              href="https://floodrestorationgeelong.au/contact" 
              target="_blank" 
              rel="noopener" 
              class="btn btn-full"
            >
              Send Message
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.contact {
  background-color: var(--white);
}

.narrow {
  max-width: 1000px;
}

.contact-box {
  display: grid;
  grid-template-columns: 0.8fr 1.2fr;
  gap: 60px;
  background: var(--white);
  padding: 40px;
  border-radius: 12px;
  box-shadow: var(--shadow-main);
}

.contact-info h2 {
  font-size: 32px;
  margin-bottom: 15px;
  color: var(--navy);
}

.contact-info > p {
  color: var(--text-light);
  margin-bottom: 40px;
}

.info-item {
  display: flex;
  gap: 15px;
  margin-bottom: 25px;
}

.info-item .icon {
  font-size: 24px;
}

.info-item strong {
  display: block;
  font-size: 14px;
  color: var(--blue);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.info-item p {
  font-size: 18px;
  font-weight: 600;
  color: var(--navy);
}

.contact-cta {
  display: flex;
  align-items: center;
}

.cta-card {
  background: var(--bg-accent);
  padding: 40px;
  border-radius: 12px;
  text-align: center;
  width: 100%;
}

.cta-card h3 {
  font-size: 22px;
  margin-bottom: 15px;
  color: var(--navy);
}

.cta-card p {
  color: var(--text-mid);
  margin-bottom: 25px;
  font-size: 15px;
}

@media (max-width: 768px) {
  .contact-box {
    grid-template-columns: 1fr;
    padding: 25px;
  }
}
</style>
