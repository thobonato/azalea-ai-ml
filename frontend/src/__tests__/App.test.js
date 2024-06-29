import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/Eco-Friendly AI Model Selector/i);
  expect(linkElement).toBeInTheDocument();
});

// Add more tests as needed