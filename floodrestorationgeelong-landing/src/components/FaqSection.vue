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
      <div class="section-title">
        <h2>Frequently Asked Questions</h2>
        <p>Expert answers to your common flood restoration concerns.</p>
      </div>

      <div class="faq-list">
        <div 
          v-for="(faq, index) in faqs" 
          :key="index" 
          class="faq-item"
          :class="{ active: activeIndex === index }"
        >
          <button class="faq-question" @click="toggle(index)">
            <span>{{ faq.question }}</span>
            <span class="icon">{{ activeIndex === index ? '−' : '+' }}</span>
          </button>
          <div class="faq-answer-wrapper" :style="{ maxHeight: activeIndex === index ? '200px' : '0' }">
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
  background-color: var(--bg-light);
}

.narrow {
  max-width: 800px;
}

.section-title {
  text-align: center;
  margin-bottom: 50px;
}

.faq-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.faq-item {
  background: var(--white);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.faq-question {
  width: 100%;
  padding: 20px 25px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: none;
  border: none;
  text-align: left;
  font-size: 17px;
  font-weight: 600;
  color: var(--secondary-color);
  cursor: pointer;
  transition: var(--transition-fast);
}

.faq-question:hover {
  background-color: rgba(0, 119, 204, 0.02);
}

.icon {
  font-size: 24px;
  color: var(--primary-color);
  line-height: 1;
}

.faq-answer-wrapper {
  overflow: hidden;
  transition: all 0.3s ease-out;
}

.faq-answer {
  padding: 0 25px 20px;
}

.faq-answer p {
  color: var(--text-light);
  font-size: 15px;
  line-height: 1.7;
}

.faq-item.active .faq-question {
  color: var(--primary-color);
}
</style>
