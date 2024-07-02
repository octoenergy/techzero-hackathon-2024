<script setup lang="ts">
import MetricItem from './MetricItem.vue'
import Header from './Header.vue'

const props = defineProps<{
  data: {
    ciTotal: number
    cost: number
    executionTime: number
    electricityUsed: number
  }
}>()
</script>

<template>
  <div class="grid-container">
    <MetricItem>
      <template #icon>
        <DocumentationIcon />
      </template>
      <template #heading>Total Execution Time</template>
      <h1 class="metric">{{ props.data.executionTime }} s</h1>
    </MetricItem>

    <MetricItem>
      <template #icon>
        <ToolingIcon />
      </template>
      <template #heading>Total Electricity Consumed</template>
      <h1 class="metric">{{ props.data.electricityUsed }} kWh</h1>
    </MetricItem>

    <MetricItem>
      <template #icon>
        <EcosystemIcon />
      </template>
      <template #heading>Total Cost</template>
      <h1 class="metric">{{ props.data.cost }} p</h1>
    </MetricItem>

    <MetricItem>
      <template #icon>
        <SupportIcon />
      </template>
      <template #heading>Total Carbon Intensity</template>
      <h1 class="metric">{{ props.data.ciTotal }} g/kWh</h1>
    </MetricItem>
  </div>
</template>

<style>
.metric {
  font-size: 30px;
  font-weight: 700;
  font-style: bold;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin: 20px;
}
</style>
