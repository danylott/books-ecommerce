import React, { useEffect } from 'react'
import { Row, Col } from 'react-bootstrap'

import { useDispatch, useSelector } from 'react-redux'

import products from '../products'
import Product from '../components/Product'
import { listProducts } from '../actions/productActions'
import Loader from '../components/Loader'
import Message from '../components/Message'

function HomeScreen() {
    const dispatch = useDispatch()
    const productList = useSelector(state => state.productList)
    const { error, loading, products, page, pages } = productList

    useEffect(() => {
        dispatch(listProducts())
    }, [dispatch])

    return (
        <div>
            <h1>
                Popular Books
            </h1>
            {loading ? <Loader />
                : error ? <Message variant='danger'>{error}</Message>
                    :
                    <Row>
                        {products.map(product => (
                            <Col xs={9} sm={7} md={5} lg={3} xl={2} key={product._id}>
                                <Product product={product} />
                            </Col>
                        ))}
                    </Row>
            }
        </div>
    )
}

export default HomeScreen
