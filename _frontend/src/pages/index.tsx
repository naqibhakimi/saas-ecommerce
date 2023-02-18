// File: pages/index.tsx
import React from 'react';
import { useQuery } from '@apollo/react-hooks';
import gql from 'graphql-tag';
import { UsersData, User } from '@/types/users';


const GET_USERS = gql`
  query {
    users {
      id
      name
      email
    }
  }
`;
const Home = () => {
  const { loading, error, data } = useQuery<UsersData>(GET_USERS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <ul>
      {data!.users.map(user => (
        <li key={user.id}>
          {user.name} ({user.email})
        </li>
      ))}
    </ul>
  );
};

export default Home;
