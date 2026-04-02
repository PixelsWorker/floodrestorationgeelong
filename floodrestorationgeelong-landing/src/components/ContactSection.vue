<template>
  <section class="contact" id="contact">
    <div class="container narrow">
      <div class="contact-box">
        <div class="contact-info">
          <h2>Contact Us</h2>
          <p>Available 24/7 for emergency flood and water damage response.</p>
          <div class="info-item">
            <span class="icon">📞</span>
            <div>
              <strong>Phone</strong>
              <p>0459 338 998</p>
            </div>
          </div>
          <div class="info-item">
            <span class="icon">📧</span>
            <div>
              <strong>Email</strong>
              <p>info@floodrestorationgeelong.au</p>
            </div>
          </div>
        </div>

        <div class="contact-form">
          <form @submit.prevent>
            <div class="form-group">
              <input type="text" placeholder="Your Name" required />
            </div>
            <div class="form-group row">
              <input type="email" placeholder="Your Email" required />
              <input type="tel" placeholder="Phone Number" required />
            </div>
            <div class="form-group row">
              <input type="text" placeholder="Suburb" required />
              <input type="text" placeholder="Post Code" required />
            </div>
            <div class="form-group">
              <textarea placeholder="How can we help?" rows="4"></textarea>
            </div>
            <button type="submit" class="btn btn-full">Send Message</button>
          </form>
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
  color: var(--secondary-color);
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
  color: var(--primary-color);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.info-item p {
  font-size: 18px;
  font-weight: 600;
  color: var(--secondary-color);
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

input, textarea {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #eee;
  border-radius: 6px;
  background-color: #f9f9f9;
  font-family: inherit;
  transition: var(--transition-fast);
}

input:focus, textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  background-color: var(--white);
}

.btn-full {
  width: 100%;
  padding: 15px;
}

@media (max-width: 768px) {
  .contact-box {
    grid-template-columns: 1fr;
    padding: 25px;
  }
  
  .form-group.row {
    grid-template-columns: 1fr;
  }
}
</style>
