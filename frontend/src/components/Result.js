import React from 'react';

const Result = ({ data }) => {
    return (
        <div className="mb-6 p-4 bg-gray-100 rounded-lg max-h-64 overflow-auto">
            <h2 className="text-xl font-semibold mb-2">Query Result</h2>
            <p className="text-gray-700 font-medium">
                {data.query_result ?? 'N/A'}
            </p>
        </div>
    );
};

export default Result;
