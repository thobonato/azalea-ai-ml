import React, { useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Graph = ({ data }) => {
    const [selectedOption, setSelectedOption] = useState('Overall');

    if (!data || !data.dyanmic_results) {
        return <div>No data available</div>;
    }

    console.log("Data for graph:", data);

    const {
        overall_cost = 0,
        overall_water = 0,
        overall_bag = 0,
        overall_feet = 0,
        overall_mistral = {},
        overall_chatgpt = {},
        overall_google = {}
    } = data.dyanmic_results;

    const transformedData = [
        {
            name: 'Overall',
            energy: overall_cost,
            water: overall_water,
            bag: overall_bag,
            feet: overall_feet,
        },
        {
            name: 'Mistral',
            energy: overall_mistral.cost || 0,
            water: overall_mistral.water || 0,
            bag: overall_mistral.bag || 0,
            feet: overall_mistral.feet || 0,
        },
        {
            name: 'ChatGPT',
            energy: overall_chatgpt.cost || 0,
            water: overall_chatgpt.water || 0,
            bag: overall_chatgpt.bag || 0,
            feet: overall_chatgpt.feet || 0,
        },
        {
            name: 'Google',
            energy: overall_google.cost || 0,
            water: overall_google.water || 0,
            bag: overall_google.bag || 0,
            feet: overall_google.feet || 0,
        },
    ];

    const noOverallData = [
        {
            name: 'Mistral',
            energy: overall_mistral.cost || 0,
            water: overall_mistral.water || 0,
            bag: overall_mistral.bag || 0,
            feet: overall_mistral.feet || 0,
        },
        {
            name: 'ChatGPT',
            energy: overall_chatgpt.cost || 0,
            water: overall_chatgpt.water || 0,
            bag: overall_chatgpt.bag || 0,
            feet: overall_chatgpt.feet || 0,
        },
        {
            name: 'Google',
            energy: overall_google.cost || 0,
            water: overall_google.water || 0,
            bag: overall_google.bag || 0,
            feet: overall_google.feet || 0,
        },
    ];

    const selectedData = transformedData.find(item => item.name === selectedOption);

    return (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-white border border-gray-200 mb-6 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow col-span-1">
                <div className="mb-4">
                    <label htmlFor="data-select" className="block text-xl font-bold text-black-700">Usage Overview</label>
                    <select
                        id="data-select"
                        value={selectedOption}
                        onChange={(e) => setSelectedOption(e.target.value)}
                        className="mt-1 block w-full pl-3 pr-10 py-2 text-med font-medium border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md shadow-sm hover:shadow-lg transition-shadow bg-gray-100"
                    >
                        <option value="Overall">Overall</option>
                        <option value="Mistral">Mistral</option>
                        <option value="ChatGPT">ChatGPT</option>
                        <option value="Google">Google</option>
                    </select>
                </div>
                <ul className="space-y-2 mb-6">
                    <li>⚡️ {selectedData?.energy?.toFixed(2) ?? 'N/A'} watt-hours used</li>
                    <li>💧 {selectedData?.water?.toFixed(3) ?? 'N/A'} ounces used</li>
                    <li>🚗 {selectedData?.feet?.toFixed() ?? 'N/A'} feet of driving used</li>
                </ul>
            </div>
            <div className="col-span-2">
                <ResponsiveContainer width="100%" height={400}>
                    <LineChart data={noOverallData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="energy" stroke="#8884d8" />
                        {/* <Line type="monotone" dataKey="water" stroke="#82ca9d" /> */}
                        {/* <Line type="monotone" dataKey="bag" stroke="#ffc658" /> */}
                        {/* <Line type="monotone" dataKey="feet" stroke="#ff7300" /> */}
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
};

export default Graph;
