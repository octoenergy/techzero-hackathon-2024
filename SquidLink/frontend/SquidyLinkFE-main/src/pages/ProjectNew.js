import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function ProjectForm() {
  const [formData, setFormData] = useState({
    name: '',
    facility_id: 0,
    skills: [], // Array of skill IDs
  });
  const [skillsList, setSkillsList] = useState([]);
  const [loadingSkills, setLoadingSkills] = useState(true);

  useEffect(() => {
    // Fetch skills from the backend
    const fetchSkills = async () => {
      try {
        const response = await fetch('http://localhost:8000/skills');
        if (!response.ok) {
          throw new Error('Failed to fetch skills');
        }
        const skillsData = await response.json();
        setSkillsList(skillsData);
        setLoadingSkills(false);
      } catch (error) {
        console.error('Error fetching skills:', error);
        setLoadingSkills(false);
      }
    };

    fetchSkills();
  }, []);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const toggleSkill = (skillId) => {
    const skillIndex = formData.skills.indexOf(skillId);
    if (skillIndex === -1) {
      setFormData({
        ...formData,
        skills: [...formData.skills, skillId],
      });
    } else {
      setFormData({
        ...formData,
        skills: formData.skills.filter((skill) => skill !== skillId),
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/project', {
        method: 'POST',
        mode: "cors",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        alert('Project created successfully.');
        navigate("/project/detail");
      } else {
        alert('Failed to create project.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while creating the project.');
    }
  };

  return (
    <div className="space-y-10 divide-y divide-gray-900/10 p-20">
      <div className="grid grid-cols-1 gap-x-8 gap-y-8 pt-10 md:grid-cols-3">
        <div className="px-4 sm:px-0">
          <h2 className="text-base font-semibold leading-7 text-gray-900">Project Information</h2>
          <p className="mt-1 text-sm leading-6 text-gray-600">Enter the project details below.</p>
        </div>

        <form onSubmit={handleSubmit} className="bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl md:col-span-2">
          <div className="px-4 py-6 sm:p-8">
            <div className="grid max-w-2xl grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-full">
                <label htmlFor="name" className="block text-sm font-medium leading-6 text-gray-900">
                  Project Name
                </label>
                <div className="mt-2">
                  <input
                    id="name"
                    name="name"
                    type="text"
                    value={formData.name}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              

              <div className="sm:col-span-full">
                <label className="block text-sm font-medium leading-6 text-gray-900">
                  Skills
                </label>
                <div className="mt-2 flex flex-wrap gap-2">
                  {skillsList.map((skill) => (
                    <button
                      key={skill.id}
                      type="button"
                      className={`inline-flex items-center px-3 py-1 bg-gray-200 rounded-md text-sm font-medium text-gray-800 ${formData.skills.includes(skill.id) ? 'bg-green-300 text-white' : ''}`}
                      onClick={() => toggleSkill(skill.id)}
                    >
                      {skill.name}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>
          <div className="flex items-center justify-end gap-x-6 border-t border-gray-900/10 px-4 py-4 sm:px-8">
            <button type="button" className="text-sm font-semibold leading-6 text-gray-900">
              Cancel
            </button>
            <button
              type="submit"
              className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >
              Create Project
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
