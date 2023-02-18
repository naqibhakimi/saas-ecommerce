import { useQuery, useMutation } from '@apollo/client';
import { GET_PRODUCTS, ADD_PRODUCT } from '@/services/products';

const IndexPage = () => {
  const { loading, error, data } = useQuery(GET_PRODUCTS);
  const [addProduct] = useMutation(ADD_PRODUCT);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error!</p>;

  return (
    <>
      <ul>
        {data.products.map((product) => (
          <li key={product.id}>
            {product.name}: {product.description}
          </li>
        ))}
      </ul>
      <button onClick={() => addProduct({ variables: { name: 'My Product', description: 'My Description' } })}>
        Add Product
      </button>
    </>
  );
}

export default IndexPage;