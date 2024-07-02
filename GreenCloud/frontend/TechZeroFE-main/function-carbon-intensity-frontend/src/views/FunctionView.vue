<script setup lang="ts">
import MetricSection from '../components/MetricSection.vue'
import CIChart from '../components/charts/CIChart.vue'
import PowerUsageChart from '../components/charts/PowerUsageChart.vue'
import Header from '../components/Header.vue'

import { ref, watch } from 'vue'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import { startOfDay } from 'date-fns'

import axios from 'axios'
import camelCaseKeys from 'camelcase-keys'

const now = new Date()
const startDate = ref(startOfDay(now))
const endDate = ref(now)
const dateFormat = 'dd/MM/yyyy HH:mm'

const data = ref(null)
const loading = ref(true)
const errored = ref(false)

const fetchData = () => {
  if (startDate.value >= endDate.value) {
    return
  }

  loading.value = true
  errored.value = false

  axios
    .get(
      `http://localhost:8080/energy?from=${startDate.value.toISOString()}&to=${endDate.value.toISOString()}&functionId=667aa0c384809f8a29ddc2f9`
    )
    .then((response) => {
      console.log(response)
      data.value = camelCaseKeys(response.data)
    })
    .catch((error) => {
      console.log(error)
      errored.value = true
    })
    .finally(() => {
      loading.value = false
    })
}

watch([startDate, endDate], fetchData)

// Fetch initial data
fetchData()
</script>

<template>
  <div class="functionView">
    <Header> </Header>
    <div class="functionContainer">
      <h2>Tech Zero x Kraken Hackathon function</h2>
      <p>ID: 667aa0c384809f8a29ddc2f9</p>
    </div>
    <div class="timeSelectContainer">
      <div class="pickerContainer">
        Start date
        <div class="datePickerContainer">
          <VueDatePicker v-model="startDate" :format="dateFormat"></VueDatePicker>
        </div>
      </div>
      <div class="pickerContainer">
        End date
        <div class="datePickerContainer">
          <VueDatePicker v-model="endDate" :format="dateFormat"></VueDatePicker>
        </div>
      </div>
    </div>

    <section v-if="errored">
      <p>Something went wrong :(</p>
    </section>
    <section class="graphSection" v-else>
      <div v-if="loading">Loading...</div>

      <div v-else>
        <MetricSection :data="camelCaseKeys(data)" />
        <div class="chartsContainer">
          <div class="chartContainer">
            <CIChart :data="camelCaseKeys(data.ciPerMinute)" />
          </div>
          <div class="chartContainer">
            <PowerUsageChart :data="camelCaseKeys(data.ciPerMinute)" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style>
.pickerContainer {
  display: flex;
  align-items: center;
  gap: 5px;
}

.chartContainer {
  background-color: white;
  border-radius: 10px;
  width: 50%;
}

.chartsContainer {
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-items: flex-start;
  margin: 20px;
}

.timeSelectContainer {
  background-color: white;
  display: flex;
  gap: 20px;
  padding: 10px;
  padding-left: 20px;
  border-bottom: 1px solid rgb(222, 222, 222);
  flex: content;
  flex-direction: row;
}

.datePickerContainer {
  width: 200px;
}

.functionContainer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  padding: 10px;
  padding-left: 20px;
  padding-right: 20px;
  border-bottom: 1px solid rgb(222, 222, 222);
}
</style>
