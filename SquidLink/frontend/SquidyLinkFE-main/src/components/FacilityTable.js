function getRandomRelevance() {
    return (Math.random() * 100).toFixed(2) + '%';
  }

  const projects = [
    { facility: 'Octopus Energy', name: 'Admn Co.', relevance: getRandomRelevance(), description: 'Installing PV panels to decrease electricity costs' },
    { facility: 'Octopus Energy', name: 'BuildWorks', relevance: getRandomRelevance(), description: 'Replacing gas boilers with heat pumps' },
    { facility: 'Octopus Energy', name: 'Construct Ltd.', relevance: getRandomRelevance(), description: 'BMS optimisation' },
    { facility: 'Octopus Energy', name: 'DevCo Solutions', relevance: getRandomRelevance(), description: 'Shaving electricity peaks' },
    { facility: 'Octopus Energy', name: 'EngiTech', relevance: getRandomRelevance(), description: 'Installing EV chargers' },
    { facility: 'Octopus Energy', name: 'HomeBuilders Inc.', relevance: getRandomRelevance(), description: 'Installing PV panels to decrease electricity costs' },
    { facility: 'Octopus Energy', name: 'InfraPro', relevance: getRandomRelevance(), description: 'Replacing gas boilers with heat pumps' },
    { facility: 'Octopus Energy', name: 'GreenBuild', relevance: getRandomRelevance(), description: 'BMS optimisation' },
    { facility: 'Octopus Energy', name: 'TechConstruct', relevance: getRandomRelevance(), description: 'Shaving electricity peaks' },
    { facility: 'Octopus Energy', name: 'EnergySolutions', relevance: getRandomRelevance(), description: 'Installing EV chargers' },
    { facility: 'Octopus Energy', name: 'EcoBuilders', relevance: getRandomRelevance(), description: 'Installing PV panels to decrease electricity costs' },
    { facility: 'Octopus Energy', name: 'FutureConstruct', relevance: getRandomRelevance(), description: 'Replacing gas boilers with heat pumps' },
    { facility: 'Octopus Energy', name: 'NextGen Builders', relevance: getRandomRelevance(), description: 'BMS optimisation' },
    { facility: 'Octopus Energy', name: 'UrbanConstruct', relevance: getRandomRelevance(), description: 'Shaving electricity peaks' },
    { facility: 'Octopus Energy', name: 'Skyline Builders', relevance: getRandomRelevance(), description: 'Installing EV chargers' },
    { facility: 'Octopus Energy', name: 'ModernBuild', relevance: getRandomRelevance(), description: 'Installing PV panels to decrease electricity costs' },
    { facility: 'Octopus Energy', name: 'PrimeConstruct', relevance: getRandomRelevance(), description: 'Replacing gas boilers with heat pumps' },
    { facility: 'Octopus Energy', name: 'EliteBuilders', relevance: getRandomRelevance(), description: 'BMS optimisation' },
    { facility: 'Octopus Energy', name: 'Advanced Construct', relevance: getRandomRelevance(), description: 'Shaving electricity peaks' },
    { facility: 'Octopus Energy', name: 'InnovativeBuilders', relevance: getRandomRelevance(), description: 'Installing EV chargers' },
  ];

  console.log(projects);




  export default function FacilityTable() {
    return (
      <div className="bg-gray-900 h-full">
        <div className="mx-auto max-w-7xl">
          <div className="bg-gray-900 py-10">
            <div className="px-4 sm:px-6 lg:px-8">
              <div className="sm:flex sm:items-center">
                <div className="sm:flex-auto">
                  <h1 className="text-base font-semibold leading-6 text-white">Projects</h1>
                </div>
              </div>
              <div className="mt-8 flow-root">
                <div className="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                  <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                    <table className="min-w-full divide-y divide-gray-700">
                      <thead>
                        <tr>
                          <th scope="col" className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-white sm:pl-0">
                            Facility
                          </th>
                          <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-white">
                            Name
                          </th>
                          <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-white">
                            Description
                          </th>
                          <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-white">
                            Relevance
                          </th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-gray-800">
                        {projects.map((project, i) => (
                          <tr key={i}>
                            <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-white sm:pl-0">
                              {project.facility}
                            </td>
                            <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-300">{project.name}</td>
                            <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-white sm:pl-0">
                            <a class="underline" href="/project/detail">
                              {project.description}
                            </a>
                            </td>
                            <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-300">
                                <>
                                <div class="w-full bg-gray-200 rounded-full dark:bg-gray-700">
                                    <div class="bg-blue-600 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full" style={{"width": project.relevance}}> {project.relevance}</div>
                                </div>
                                </>
                            </td>
                            <td className="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                                <div className="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
                              <a href="/bid/new">
                                <button
                                    type="button"
                                    className="block rounded-md bg-indigo-500 px-3 py-2 text-center text-sm font-semibold text-white hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
                                >
                                    Bid
                                </button>
                              </a>
                                </div>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
