// Copyright (C) 2018-2023 Intel Corporation
// SPDX-License-Identifier: Apache-2.0
//

#pragma once

#include "openvino/frontend/pytorch/decoder.hpp"
#include "translate_session.hpp"

namespace ov {
namespace frontend {
namespace pytorch {

class InputModel : public ov::frontend::InputModel {
    friend class ::ov::frontend::pytorch::TranslateSession;
    std::shared_ptr<TorchDecoder> m_model;

public:
    explicit InputModel(std::shared_ptr<TorchDecoder> model) : m_model(model) {}
    // TODO: pass telemetry extension to this ctor
};

}  // namespace pytorch
}  // namespace frontend
}  // namespace ov
