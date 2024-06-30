import React from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Graph = ({ data }) => {
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

    return (
        <ResponsiveContainer width="100%" height={400}>
            <LineChart data={transformedData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
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
    );
};

export default Graph;