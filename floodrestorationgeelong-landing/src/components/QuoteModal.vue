<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

const WP_API = 'https://floodrestorationgeelong.au/wp-json/frg/v1/contact'

const submitted = ref(false)
const loading = ref(false)
const errorMsg = ref('')
const honeypot = ref('')

const form = reactive({
  name: '',
  phone: '',
  email: '',
  suburb: '',
  postcode: '',
  message: ''
})

async function handleSubmit() {
  if (honeypot.value) return
  
  loading.value = true
  errorMsg.value = ''
  
  try {
    const res = await fetch(WP_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name:    form.name,
        phone:   form.phone,
        email:   form.email,
        suburb:  `${form.suburb}${form.postcode ? ' ' + form.postcode : ''}`,
        message: form.message
      })
    })
    
    const data = await res.json()
    
    if (data.success) {
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

function closePopup() {
  emit('close')
  // Reset form on close if successfully submitted
  if (submitted.value) {
    resetForm()
  }
}

function resetForm() {
  submitted.value = false
  errorMsg.value = ''
  Object.assign(form, { name: '', phone: '', email: '', suburb: '', postcode: '', message: '' })
}

// Handle Escape Key
const handleEsc = (e) => {
  if (e.key === 'Escape' && props.isOpen) {
    closePopup()
  }
}

onMounted(() => window.addEventListener('keydown', handleEsc))
onUnmounted(() => window.removeEventListener('keydown', handleEsc))
</script>

<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="isOpen" class="modal-overlay" @click.self="closePopup">
        <Transition name="zoom">
          <div v-if="isOpen" class="modal-container">
            <button class="modal-close" @click="closePopup" aria-label="Close Modal">&times;</button>
            
            <!-- Success State -->
            <div v-if="submitted" class="success-wrap">
              <div class="success-icon">✅</div>
              <h3>Request Received!</h3>
              <p>Thanks <strong>{{ form.name }}</strong>, our team will be in touch shortly to provide your quote.</p>
              <div class="success-actions">
                <a href="tel:0459338998" class="btn btn-call">📞 Call 0459 338 998</a>
                <button class="btn-done" @click="closePopup">Close Window</button>
              </div>
            </div>

            <!-- Form State -->
            <div v-else class="modal-content">
              <div class="modal-header">
                <h2>Get a Quote</h2>
                <p>Tell us about your situation for a fast response.</p>
              </div>

              <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>

              <form @submit.prevent="handleSubmit" novalidate>
                <input type="text" v-model="honeypot" style="display:none !important" tabindex="-1" autocomplete="off" />

                <div class="form-group full-width">
                  <label for="modal-name">Full Name *</label>
                  <input id="modal-name" v-model="form.name" type="text" placeholder="Your Name" required />
                </div>

                <div class="form-row">
                  <div class="form-group">
                    <label for="modal-email">Email Address</label>
                    <input id="modal-email" v-model="form.email" type="email" placeholder="example@email.com" />
                  </div>
                  <div class="form-group">
                    <label for="modal-phone">Phone Number *</label>
                    <input id="modal-phone" v-model="form.phone" type="tel" placeholder="04XX XXX XXX" required />
                  </div>
                </div>

                <div class="form-row">
                  <div class="form-group">
                    <label for="modal-suburb">Suburb</label>
                    <input id="modal-suburb" v-model="form.suburb" type="text" placeholder="e.g. Geelong" />
                  </div>
                  <div class="form-group">
                    <label for="modal-postcode">Post Code</label>
                    <input id="modal-postcode" v-model="form.postcode" type="text" placeholder="3220" />
                  </div>
                </div>

                <div class="form-group full-width">
                  <label for="modal-message">How can we help?</label>
                  <textarea id="modal-message" v-model="form.message" rows="3" placeholder="Briefly describe the water damage or service needed..."></textarea>
                </div>

                <button type="submit" class="btn btn-submit-quote" :disabled="loading || !form.name || !form.phone">
                  <span v-if="loading" class="spinner"></span>
                  <span v-else>SEND REQUEST →</span>
                </button>
              </form>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(7, 26, 48, 0.7);
  backdrop-filter: blur(8px);
  z-index: 9000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-container {
  background: var(--white);
  width: 100%;
  max-width: 580px;
  border-radius: 16px;
  box-shadow: 0 25px 60px rgba(0,0,0,0.3);
  position: relative;
  overflow: hidden;
}

.modal-close {
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 32px;
  color: var(--navy);
  cursor: pointer;
  z-index: 10;
  transition: transform 0.2s;
}
.modal-close:hover {
  transform: rotate(90deg) scale(1.2);
  color: var(--red);
}

.modal-content,
.success-wrap {
  padding: 45px;
}

.modal-header h2 {
  font-size: 32px;
  color: var(--navy);
  margin-bottom: 8px;
  font-weight: 800;
}
.modal-header p {
  color: var(--text-light);
  font-size: 15px;
  margin-bottom: 30px;
}

.error-msg {
  background: #fff0f0;
  color: #e31e24;
  padding: 12px;
  border-radius: 6px;
  margin-bottom: 20px;
  font-size: 14px;
  font-weight: 600;
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
  margin-bottom: 15px;
}
.form-group label {
  font-size: 13px;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 5px;
}
.form-group input,
.form-group textarea {
  border: 1.5px solid #e1e5ea;
  border-radius: 6px;
  padding: 11px 14px;
  font-size: 15px;
  transition: all 0.2s;
  outline: none;
}
.form-group input:focus,
.form-group textarea:focus {
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(0, 124, 190, 0.1);
}

.btn-submit-quote {
  width: 100%;
  background: var(--red);
  color: var(--white);
  padding: 16px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 800;
  cursor: pointer;
  margin-top: 10px;
  transition: all 0.3s;
}
.btn-submit-quote:hover:not(:disabled) {
  background: var(--navy);
  transform: translateY(-2px);
}
.btn-submit-quote:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Success */
.success-wrap {
  text-align: center;
  padding: 60px 45px;
}
.success-icon { font-size: 64px; margin-bottom: 20px; }
.success-wrap h3 { font-size: 26px; color: var(--navy); margin-bottom: 12px; }
.success-wrap p { color: var(--text-mid); margin-bottom: 30px; font-size: 17px; }

.success-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.btn-call {
  background: var(--red);
  color: var(--white);
  padding: 15px;
  border-radius: 6px;
  font-weight: 700;
}
.btn-done {
  background: none;
  border: none;
  color: var(--text-light);
  text-decoration: underline;
  cursor: pointer;
}

/* Transitions */
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.zoom-enter-active, .zoom-leave-active { transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); }
.zoom-enter-from, .zoom-leave-to { opacity: 0; transform: scale(0.9); }

@media (max-width: 768px) {
  .form-row { grid-template-columns: 1fr; }
  .modal-container { border-radius: 0; height: 100%; overflow-y: auto; }
}
</style>
