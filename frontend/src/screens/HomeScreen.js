import React from 'react'
import { Row, Col } from 'react-bootstrap'

import products from '../products'
import Product from '../components/Product'

function HomeScreen() {
    return (
        <div>
            <h1>
                Popular Books
            </h1>
            <Row>
                {products.map(product => (
                    <Col  xs={9} sm={7} md={5} lg={3} xl={2} key={product._id}>
                        <Product product={product}/>
                    </Col>
                ))}
            </Row>
        </div>
    )
}

export default HomeScreen
