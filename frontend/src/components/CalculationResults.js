import React from 'react';

// simplified for sake of making work

const CalculationResults = ({ result }) => (
  <pre>{JSON.stringify(result, null, 2)}</pre>
);

export default CalculationResults;