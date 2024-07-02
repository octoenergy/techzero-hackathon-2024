const stats = [
    { name: 'Carbon dioxide emissions:', value: '5.6' , unit: 'tCO2e per year '},
    { name: 'Total energy costs', value: '54k', unit: '£ per year' },
    { name: 'peak electricity import', value: '250 ', unit: 'kW' },
    { name: 'current export', value: '20', unit: 'kW' },
  ]
  
  export default function StatsHeader() {
    return (
      <div className="bg-white-900">
        <div className="mx-auto max-w-7xl">
          <div className="grid grid-cols-1 gap-px bg-white/5 sm:grid-cols-2 lg:grid-cols-4">
            {stats.map((stat) => (
              <div key={stat.name} className="bg-white-400 px-4 py-6 sm:px-6 lg:px-8">
                <p className="text-sm font-medium leading-6 text-black-400">{stat.name}</p>
                <p className="mt-2 flex items-baseline gap-x-2">
                  <span className="text-4xl font-semibold tracking-tight text-black">{stat.value}</span>
                  {stat.unit ? <span className="text-sm text-gray-400">{stat.unit}</span> : null}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    )
  }