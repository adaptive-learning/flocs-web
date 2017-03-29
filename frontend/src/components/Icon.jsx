import React, { PropTypes } from 'react';
import Image from './Image';

export default function Icon({ name }) {
  const iconStyle = {
    height: '1em',
    position: 'relative',
    top: '0.1em',
  };

  return (
    <Image imageId={`icon-${name}`} style={iconStyle} />
  );
}

Icon.propTypes = {
  name: PropTypes.string.isRequired,
};
