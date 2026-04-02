<script setup>
import { ref } from 'vue'

const activeIndex = ref(0)

const faqs = [
  {
    question: 'What should I do immediately after finding water damage?',
    answer: 'Your first priority is safety. Stop the water if possible, turn off electricity in affected areas, call for professional help (0459 338 998), and move valuables to a dry area.'
  },
  {
    question: 'How much does emergency water damage repair cost in Geelong?',
    answer: 'The cost depends on area size, water type (clean/grey/black), and duration. we offer a transparent, on-site assessment and a detailed quote before any work commences.'
  },
  {
    question: 'How long does the water damage restoration process take?',
    answer: 'Initial extraction takes hours, but structural drying and dehumidification usually last 3 to 5 days ensuring no hidden moisture remains.'
  },
  {
    question: 'Is it safe to stay in my house after water damage?',
    answer: 'It depends on the extent. Clean water leaks might be safe, but contaminated water (sewage/flood) or structural damage makes it unsafe. Our technicians will assess and advise.'
  },
  {
    question: 'Will my insurance cover the cost of water damage repairs?',
    answer: 'Most Australian policies cover sudden/accidental damage. We work with all major insurers in Geelong to supply documents and reports to help your claim.'
  }
]

const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index
}
</script>

<template>
  <section class="faq">
    <div class="container narrow">
      <div class="section-header">
        <label class="section-label">Common Questions</label>
        <h2 class="section-title">Frequently Asked Questions - Water Damage Restoration Geelong</h2>
        <p class="section-subtitle">Expert answers to your most common flood restoration and water damage concerns.</p>
      </div>

      <div class="faq-list">
        <div 
          v-for="(faq, index) in faqs" 
          :key="index" 
          class="faq-item"
          :class="{ active: activeIndex === index }"
        >
          <button class="faq-question" @click="toggle(index)">
            <span class="q-icon">{{ activeIndex === index ? '−' : '+' }}</span>
            <span class="q-text">{{ faq.question }}</span>
          </button>
          <div class="faq-answer-wrapper" :style="{ maxHeight: activeIndex === index ? '300px' : '0' }">
            <div class="faq-answer">
              <p>{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.faq {
  background-color: var(--soft-blue);
  padding: 100px 0;
}

.narrow {
  max-width: 950px;
}

.faq-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.faq-item {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  transition: var(--transition-fast);
}

.faq-item.active {
  border-color: var(--blue);
  box-shadow: 0 5px 15px rgba(0, 119, 204, 0.05);
}

.faq-question {
  width: 100%;
  padding: 22px 30px;
  display: flex;
  align-items: center;
  gap: 20px;
  background: none;
  border: none;
  text-align: left;
  font-size: clamp(15px, 2vw, 17px);
  font-weight: 700;
  color: var(--navy);
  cursor: pointer;
  transition: var(--transition-fast);
}

.q-icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--blue);
  color: var(--blue);
  border-radius: 50%;
  font-weight: 800;
  font-size: 16px;
}

.active .q-icon {
  background: var(--blue);
  color: var(--white);
}

.faq-answer-wrapper {
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.faq-answer {
  padding: 0 30px 30px 74px; /* Offset to align with q-text */
}

.faq-answer p {
  color: var(--text-mid);
  font-size: 15.5px;
  line-height: 1.8;
  border-top: 1px solid var(--bg-soft-blue);
  padding-top: 15px;
}

@media (max-width: 768px) {
  .faq-answer {
    padding: 0 25px 25px 25px;
  }
  .faq-question {
    padding: 20px;
  }
}
</style>
