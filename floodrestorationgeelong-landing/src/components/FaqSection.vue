<script setup>
import { ref } from 'vue'

const activeIndex = ref(0)

const faqs = [
  {
    question: 'What should I do immediately after finding water damage?',
    answer: '<p>Your first priority is safety. You should act immediately and safely by:</p><ul><li><b>Stop the Water:</b> If possible, shut off the main water valve to your property.</li><li><b>Turn Off Electricity:</b> To prevent electrical hazards, turn off the power at your circuit breaker box in affected areas.</li><li><b>Call for Professional Help:</b> Contact our 24/7 team on 0459 338 998. The faster we begin, the less damage occurs.</li><li><b>Move Valuables:</b> Move furniture and electronics to dry areas. Place foil under furniture legs to prevent staining.</li></ul>'
  },
  {
    question: 'How much does emergency water damage repair cost in Geelong?',
    answer: 'The cost depends on several factors: the size of the area, the type of water (clean, grey, or black), how long it has been present, and materials affected. We offer a transparent, on-site assessment and a detailed quote before any work commences. Investing in professional restoration is much more affordable than dealing with structural issues and mould later.'
  },
  {
    question: 'How long does the water damage restoration process take?',
    answer: 'The timeline varies with severity. Initial extraction takes hours, but structural drying and dehumidification usually last 3 to 5 days. we use advanced equipment to ensure complete dryness before completion, with no hidden moisture left.'
  },
  {
    question: 'Is it safe to stay in my house after water damage?',
    answer: 'This depends on the extent and type of damage. If the water is from a clean source (like a burst pipe), it may be safe. However, if there is significant flooding, structural damage, or contaminated water (sewage/floodwater), it is often unsafe. Our technicians will assess the risk and advise you on-site.'
  },
  {
    question: 'Will my insurance cover the cost of water damage repairs?',
    answer: 'Most Australian home insurance policies cover sudden and accidental water damage. With over 20 years of experience working with major insurers in Geelong, we provide the necessary documentation, moisture readings, and reports to facilitate your claim. We recommend contacting your insurer for specific policy details.'
  },
  {
    question: 'Can I clean up minor water damage myself?',
    answer: 'Handling a small leak with towels and a fan might seem tempting, but it’s risky. Water can seep into sub-flooring and wall cavities, creating hidden mould in 24-48 hours. Professionals use specialised equipment to detect and remove all moisture, ensuring the problem is fully solved.'
  },
  {
    question: 'What is the difference between clean water, grey water, and black water?',
    answer: 'Understanding water categories is crucial for safety:<ul><li><b>Category 1 (Clean Water):</b> From sanitary sources like burst pipes. Usually harmless but can contaminate if left standing.</li><li><b>Category 2 (Grey Water):</b> Contains contaminants (e.g., dishwasher overflow) and can cause illness.</li><li><b>Category 3 (Black Water):</b> Highly unsanitary (sewage/overland flooding) containing dangerous pathogens. Requires specialised PPE and procedures.</li></ul>'
  },
  {
    question: 'How do you prevent mould from growing after a flood?',
    answer: 'Speed is key. We prevent mould by:<ul><li><b>Rapid Extraction:</b> Immediate removal of standing water.</li><li><b>Structural Drying:</b> Using industrial air movers to dry the structure quickly.</li><li><b>Antimicrobial Treatment:</b> Applying professional-grade, non-toxic agents to kill spores.</li><li><b>Moisture Monitoring:</b> Verifying humidity levels are safe.</li></ul>'
  },
  {
    question: 'What does "IICRC certified" mean and why is it important?',
    answer: 'The IICRC sets the global standard for the restoration industry. An IICRC-certified technician has completed extensive training on water damage restoration. Choosing an IICRC-certified company ensures hiring professionals who follow top safety and quality standards.'
  },
  {
    question: 'Will there be a bad smell after the water damage, and can you remove it?',
    answer: 'A musty odour is a sign of moisture and microbial activity. It won’t disappear on its own. Our process involves thorough cleaning, sanitisation, and professional deodorisation with specialised equipment like hydroxyl generators to remove these odours at their source.'
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
          <div class="faq-answer-wrapper" :style="{ maxHeight: activeIndex === index ? '800px' : '0' }">
            <div class="faq-answer">
              <div v-html="faq.answer" class="faq-html-content"></div>
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

.faq-html-content {
  color: var(--text-mid);
  font-size: 15.5px;
  line-height: 1.8;
  border-top: 1px solid var(--bg-soft-blue);
  padding-top: 15px;
}

.faq-html-content :deep(ul) {
  margin: 15px 0 0 20px;
  padding: 0;
}

.faq-html-content :deep(li) {
  margin-bottom: 8px;
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
