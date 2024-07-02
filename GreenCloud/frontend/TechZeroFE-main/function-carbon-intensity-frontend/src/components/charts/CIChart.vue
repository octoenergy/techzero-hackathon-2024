<template>
  <div class="card" style="position: relative; width: 100%">
    <Chart type="line" :data="chartData" :height="400" :options="chartOptions" />
  </div>
</template>

<script setup lang="ts">
import { format } from 'date-fns'
const props = defineProps<{
  data: {
    carbonIntensity: number
    timestamp: string
  }[]
}>()

import Chart from 'primevue/chart'

import { ref, onMounted } from 'vue'

onMounted(() => {
  chartData.value = setChartData()
  chartOptions.value = setChartOptions()
})

const chartData = ref()
const chartOptions = ref()

console.log(props.data)

const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement)

  return {
    labels: props.data.map((element) => format(new Date(element.timestamp), 'dd/MM HH:mm')),
    datasets: [
      {
        label: 'Carbon intensity',
        data: props.data.map((element) => element.carbonIntensity),
        fill: false,
        borderColor: '#1FCCCC', // documentStyle.getPropertyValue('--p-gray-500'),
        tension: 0.4
      }
    ]
  }
}
const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement)
  const textColor = documentStyle.getPropertyValue('--p-text-color')
  const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color')
  const surfaceBorder = documentStyle.getPropertyValue('--p-content-border-color')

  return {
    maintainAspectRatio: false,
    aspectRatio: 0.6,
    plugins: {
      legend: {
        display: false
      },
      title: {
        display: true,
        font: {
          size: 20
        },
        text: 'Carbon Intensity [g/kWh]'
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      },
      y: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      }
    }
  }
}
</script>
