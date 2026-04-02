<script setup>
import { ref } from 'vue'

const steps = [
  {
    title: 'Emergency Contact & Rapid Despatch (Your First Call)',
    content: 'The moment you contact us, our process starts. Our friendly, knowledgeable team will ask a few key questions to understand the situation (e.g., the source of the water, the areas affected). We will then immediately deploy our nearest emergency response team to your location.',
    isOpen: true
  },
  {
    title: 'On-Site Inspection & Damage Assessment',
    content: 'Upon arrival, our lead technician will perform a comprehensive inspection. Using advanced moisture detection tools, we will assess the full extent of water damage, including areas with hidden moisture. We classify the water as Category 1, 2, or 3 to determine the appropriate sanitisation steps and create a detailed restoration plan.',
    isOpen: false
  },
  {
    title: 'Rapid Water Extraction',
    content: 'This is the most critical step to prevent further damage. Using our powerful extraction equipment, we will remove thousands of litres of standing water from your property. This immediate removal is crucial for saving carpets, underlay, and subflooring.',
    isOpen: false
  },
  {
    title: 'Removal of Non-Salvageable Items & Debris',
    content: 'Our team will carefully remove any items or building materials (like saturated plasterboard or carpet underlay) that are deemed non-salvageable according to IICRC standards. This helps expedite the drying process and ensures a clean, safe environment.',
    isOpen: false
  },
  {
    title: 'Structural Drying & Dehumidification',
    content: 'Once the bulk water is gone, we strategically place our industrial air movers and LGR dehumidifiers. This creates an optimal drying environment, pulling moisture from porous materials like wood, drywall, and concrete. This is not just about drying the surface; it’s about returning the entire structure to its normal equilibrium moisture content.',
    isOpen: false
  },
  {
    title: 'Cleaning, Sanitising & Odour Control',
    content: 'Water damage can leave behind contaminants and unpleasant odours. We conduct a thorough cleaning of all affected surfaces. Depending on the water category, we apply professional antimicrobial treatments to prevent mould growth and utilise specialised equipment such as hydroxyl generators or thermal foggers to remove any lingering odours.',
    isOpen: false
  },
  {
    title: 'Continuous Monitoring & Final Inspections',
    content: 'Our job isn’t finished when the equipment is placed. Our technicians will return to your property regularly to monitor the drying process, taking moisture readings and adjusting equipment as needed to ensure optimal results. Once we certify that your property is completely dry according to IICRC standards, we conduct a final walkthrough with you.',
    isOpen: false
  }
]

const activeIndex = ref(0)

const toggleStep = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index
}
</script>

<template>
  <section class="how-it-works">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Our IICRC-Certified Flood Restoration Process:</h2>
        <h3 class="process-subtitle">A Step-by-Step Guide to Recovery</h3>
        <p class="section-subtitle">We value transparency. Knowing what to expect can greatly lessen stress during a crisis. Here is the proven, step-by-step process our qualified technicians adhere to on every job.</p>
      </div>

      <div class="process-content">
        <div class="accordion-column">
          <div 
            v-for="(step, index) in steps" 
            :key="index" 
            class="accordion-item"
            :class="{ 'is-active': activeIndex === index }"
          >
            <button class="accordion-header" @click="toggleStep(index)">
              <span class="step-title">{{ step.title }}</span>
              <span class="icon">
                <svg v-if="activeIndex === index" viewBox="0 0 448 512" width="14"><path fill="currentColor" d="M416 208H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h384c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"/></svg>
                <svg v-else viewBox="0 0 448 512" width="14"><path fill="currentColor" d="M416 208H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h384c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32zM416 208v32h-384v-32h384z"/></svg>
              </span>
            </button>
            <div class="accordion-body">
              <div class="accordion-inner">
                <p>{{ step.content }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="image-column">
          <div class="featured-image">
            <img 
              src="https://floodrestorationgeelong.au/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-05-at-12.39.42-PM-768x1024.jpeg" 
              alt="Professional Flood Restoration in Progress"
            />
            <div class="image-overlay">
              <span class="badge">Professional Quality</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.how-it-works {
  background-color: var(--white);
  padding: 100px 0;
}

.process-subtitle {
  font-size: 28px;
  color: var(--blue);
  margin-bottom: 20px;
  font-weight: 700;
}

.process-content {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 60px;
  align-items: start;
}

.accordion-column {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.accordion-item {
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.accordion-item.is-active {
  border-color: var(--blue);
  box-shadow: 0 5px 20px rgba(0, 119, 204, 0.08);
}

.accordion-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 22px 25px;
  background: var(--bg-accent);
  border: none;
  cursor: pointer;
  text-align: left;
  transition: background 0.3s;
}

.accordion-item.is-active .accordion-header {
  background: var(--white);
}

.step-title {
  font-family: 'Poppins', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--navy);
}

.accordion-item.is-active .step-title {
  color: var(--blue);
}

.accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.accordion-item.is-active .accordion-body {
  max-height: 500px;
}

.accordion-inner {
  padding: 0 25px 25px;
  font-size: 15px;
  color: var(--text-mid);
  line-height: 1.8;
}

.featured-image {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-main);
}

.featured-image img {
  width: 100%;
  height: auto;
  display: block;
}

.image-overlay {
  position: absolute;
  bottom: 20px;
  right: 20px;
}

.badge {
  background: var(--blue);
  color: var(--white);
  padding: 8px 15px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
}

@media (max-width: 1100px) {
  .process-content {
    grid-template-columns: 1fr;
    gap: 50px;
  }
  
  .image-column {
    max-width: 600px;
    margin: 0 auto;
  }
}

@media (max-width: 768px) {
  .how-it-works {
    padding: 60px 0;
  }
  
  .process-subtitle {
    font-size: 22px;
  }
  
  .accordion-header {
    padding: 18px 20px;
  }
  
  .step-title {
    font-size: 15px;
  }
}
</style>
