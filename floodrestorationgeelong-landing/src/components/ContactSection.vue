<script setup>
import { ref, reactive } from 'vue'

const WP_API = 'https://floodrestorationgeelong.au/wp-json/contact-form-7/v1/contact-forms/8345c53/feedback'

const submitted = ref(false)
const loading = ref(false)
const errorMsg = ref('')
const honeypot = ref('') // Anti-spam hidden field

const form = reactive({
  name: '',
  phone: '',
  email: '',
  suburb: '',
  postcode: '',
  message: ''
})

async function handleSubmit() {
  if (honeypot.value) return // If honeypot is filled, it's a bot
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    const formData = new FormData()
    formData.append('your-name',     form.name)
    formData.append('your-phone',    form.phone)
    formData.append('your-email',    form.email)
    formData.append('your-suburb',   form.suburb)
    formData.append('your-postcode', form.postcode)
    formData.append('your-message',  form.message)

    const res = await fetch(WP_API, {
      method: 'POST',
      body: formData // No headers needed for FormData
    })
    
    const data = await res.json()
    
    if (data.status === 'mail_sent') {
      submitted.value = true
    } else {
      errorMsg.value = data.message || 'Something went wrong. Please call us directly.'
    }
  } catch (error) {
    console.error('Submission failed:', error)
    errorMsg.value = 'Network error. Please call us on 0459 338 998.'
  } finally {
    loading.value = false
  }
}

function resetForm() {
  submitted.value = false
  errorMsg.value = ''
  Object.assign(form, { name: '', phone: '', email: '', suburb: '', postcode: '', message: '' })
}
</script>

<template>
  <section class="contact" id="contact">
    <div class="container">
      <div class="contact-grid">

        <!-- LEFT: Info -->
        <div class="contact-info">
          <label class="section-label">Get In Touch</label>
          <h2 class="contact-title">Contact us</h2>
          <p>Available <strong>24/7</strong> for emergency flood and water damage response across Geelong and surrounds.</p>

          <div class="info-block">
            <div class="info-item">
              <span class="info-icon">📞</span>
              <div>
                <span class="info-label">Emergency Hotline</span>
                <a href="tel:0459338998" class="info-value">0459 338 998</a>
              </div>
            </div>
            <div class="info-item">
              <span class="info-icon">📧</span>
              <div>
                <span class="info-label">Email Address</span>
                <a href="mailto:info@floodrestorationgeelong.au" class="info-value">info@floodrestorationgeelong.au</a>
              </div>
            </div>
            <div class="info-item">
              <span class="info-icon">🕐</span>
              <div>
                <span class="info-label">Hours</span>
                <span class="info-value">24/7 Emergency Response</span>
              </div>
            </div>
            <div class="info-item">
              <span class="info-icon">📍</span>
              <div>
                <span class="info-label">Service Area</span>
                <span class="info-value">Geelong & Surrounds</span>
              </div>
            </div>
          </div>

          <a href="tel:0459338998" class="btn btn-call">
            📞 Call Now — 0459 338 998
          </a>
        </div>

        <!-- RIGHT: Form -->
        <div class="contact-form-wrap">
          <Transition name="fade-slide" mode="out-in">
            <div v-if="!submitted" key="form" class="form-card">
              <h2 class="form-main-heading">Contact us</h2>

              <!-- Error Area -->
              <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>

              <form @submit.prevent="handleSubmit" novalidate>
                <!-- Honeypot (bot trap) -->
                <input type="text" v-model="honeypot" style="display:none !important" tabindex="-1" autocomplete="off" />

                <!-- Row 1: Name -->
                <div class="form-group full-width">
                  <label for="name">Name</label>
                  <input
                    id="name"
                    v-model="form.name"
                    type="text"
                    placeholder="Name"
                    required
                  />
                </div>

                <!-- Row 2: Email & Phone -->
                <div class="form-row">
                  <div class="form-group">
                    <label for="email">Email</label>
                    <input
                      id="email"
                      v-model="form.email"
                      type="email"
                      placeholder="Email"
                    />
                  </div>
                  <div class="form-group">
                    <label for="phone">Phone No</label>
                    <input
                      id="phone"
                      v-model="form.phone"
                      type="tel"
                      placeholder="Phone No"
                    />
                  </div>
                </div>

                <!-- Row 3: Suburb & Post Code -->
                <div class="form-row">
                  <div class="form-group">
                    <label for="suburb">Suburb</label>
                    <input
                      id="suburb"
                      v-model="form.suburb"
                      type="text"
                      placeholder="Suburb"
                    />
                  </div>
                  <div class="form-group">
                    <label for="postcode">Post Code</label>
                    <input
                      id="postcode"
                      v-model="form.postcode"
                      type="text"
                      placeholder="Post Code"
                    />
                  </div>
                </div>

                <!-- Row 4: Message -->
                <div class="form-group full-width">
                  <label for="message">Message</label>
                  <textarea
                    id="message"
                    v-model="form.message"
                    rows="3"
                    placeholder="Message"
                  ></textarea>
                </div>

                <button type="submit" class="btn btn-send-now" :disabled="loading || !form.name">
                  <span v-if="loading" class="spinner"></span>
                  <span v-else>SEND</span>
                </button>
              </form>
            </div>

            <!-- Success State -->
            <div v-else key="success" class="success-card">
              <div class="success-icon">✅</div>
              <h3>Message Received!</h3>
              <p>Thanks <strong>{{ form.name }}</strong>, we'll be in touch shortly. For urgent emergencies call us directly.</p>
              <a href="tel:0459338998" class="btn btn-call" style="margin-bottom: 20px;">📞 0459 338 998</a>
              <button class="btn-reset" @click="resetForm">Send another message</button>
            </div>
          </Transition>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
.contact {
  background-color: var(--white);
  padding: 100px 0;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.3fr;
  gap: 80px;
  align-items: start;
}

/* LEFT */
.contact-title {
  font-size: clamp(32px, 5vw, 42px);
  color: var(--navy);
  margin: 10px 0 16px;
  font-weight: 800;
  line-height: 1.1;
}

.contact-info > p {
  color: var(--text-mid);
  margin-bottom: 35px;
  font-size: 17px;
}

.info-block {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 40px;
}

.info-item {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.info-icon {
  font-size: 24px;
}

.info-label {
  display: block;
  font-size: 11px;
  font-weight: 700;
  color: var(--blue);
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 4px;
}

.info-value {
  font-size: 18px;
  font-weight: 700;
  color: var(--navy);
}

a.info-value:hover {
  color: var(--blue);
}

.btn-call {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background-color: var(--red);
  color: var(--white);
  padding: 16px 32px;
  border-radius: 6px;
  font-size: 17px;
  font-weight: 800;
  text-decoration: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  width: 100%;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(227, 30, 36, 0.15);
}

.btn-call:hover {
  background-color: var(--navy);
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(27, 50, 82, 0.2);
}

/* RIGHT */
.form-card,
.success-card {
  background: #f4f8fc;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 5px 25px rgba(0,0,0,0.04);
}

.form-main-heading {
  font-size: 48px;
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 30px;
  letter-spacing: -1px;
}

.error-msg {
  background: #fff0f0;
  color: #e31e24;
  padding: 12px 14px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 20px;
  border-left: 4px solid #e31e24;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
  margin-bottom: 12px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 12px;
}

.form-group.full-width {
  width: 100%;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-light);
  margin-bottom: 6px;
  padding-left: 2px;
}

.form-group input,
.form-group textarea {
  background: var(--white);
  border: 1px solid #c2c9d2;
  border-radius: 4px;
  padding: 12px 14px;
  font-size: 15px;
  color: var(--navy);
  transition: all 0.2s ease;
  outline: none;
  width: 100%;
}

.form-group input::placeholder,
.form-group textarea::placeholder {
  color: #c2c9d2;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #7b8ea3;
  box-shadow: 0 0 0 4px rgba(123, 142, 163, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.btn-send-now {
  width: 100%;
  background: var(--red);
  color: var(--white);
  padding: 18px;
  border: none;
  border-radius: 6px;
  font-size: 18px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 15px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.btn-send-now:hover:not(:disabled) {
  background: var(--red-dark);
  transform: scale(1.01);
}

.btn-send-now:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.spinner {
  width: 22px;
  height: 22px;
  border: 3px solid rgba(255,255,255,0.4);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Transitions */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.fade-slide-enter-from { opacity: 0; transform: translateX(20px); }
.fade-slide-leave-to { opacity: 0; transform: translateX(-20px); }

/* Success */
.success-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 60px 40px;
}

.success-icon {
  font-size: 64px;
  margin-bottom: 24px;
}

.success-card h3 {
  font-size: 24px;
  margin-bottom: 12px;
}

.success-card p {
  color: var(--text-mid);
  margin-bottom: 30px;
  font-size: 18px;
}

.btn-reset {
  background: none;
  border: none;
  color: var(--blue);
  font-size: 14px;
  cursor: pointer;
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 1200px) {
  .contact-grid {
    gap: 40px;
    grid-template-columns: 1fr 1.2fr;
  }
}

@media (max-width: 992px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 50px;
  }
  .form-main-heading {
    text-align: center;
    font-size: 38px;
  }
}

@media (max-width: 768px) {
  .contact { padding: 70px 0; }
  .form-row { grid-template-columns: 1fr; }
  .form-card { padding: 25px; }
  .contact-info h2 { text-align: center; }
  .contact-info > p { text-align: center; }
  .info-item { justify-content: center; }
}
</style>
