import { useQuery, useMutation } from '@apollo/client';
import { GET_PRODUCTS, ADD_PRODUCT } from '@/services/products';
import { _GET_USERS } from '../services/customer';

import { convertEdgeToList } from '@/utils/helpers';

const IndexPage = () => {
  
  const { loading, error, data } = useQuery(_GET_USERS);
  // const [addProduct] = useMutation(ADD_PRODUCT);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error! {JSON.stringify(data, null, 2)}</p>;

  return (
    <>
     <div className="text-3xl font-bold underline pb-4">Hello</div>
      <ul>
        {convertEdgeToList(data.users.edges).map((node) => (
          <li key={node.id}>
            {node.firstName}: {node.lastName}
          </li>
        ))}
      </ul>
      {/* <button onClick={() => addProduct({ variables: { name: 'My Product', description: 'My Description' } })}>
        Add Product
      </button> */}
    </>
  );
}

export default IndexPage;