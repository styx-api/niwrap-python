# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DSVM_LINPREDICT_METADATA = Metadata(
    id="75accbcc401ca78691df247e44440c27677dbbec.boutiques",
    name="3dsvm_linpredict",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dsvmLinpredictParameters = typing.TypedDict('V3dsvmLinpredictParameters', {
    "__STYXTYPE__": typing.Literal["3dsvm_linpredict"],
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "weight_vector": InputPathType,
    "input_dataset": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "3dsvm_linpredict": v_3dsvm_linpredict_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "3dsvm_linpredict": v_3dsvm_linpredict_outputs,
    }.get(t)


class V3dsvmLinpredictOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dsvm_linpredict(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout_output: OutputPathType
    """The result is a number printed to stdout"""


def v_3dsvm_linpredict_params(
    weight_vector: InputPathType,
    input_dataset: str,
    mask_dataset: InputPathType | None = None,
) -> V3dsvmLinpredictParameters:
    """
    Build parameters.
    
    Args:
        weight_vector: Weight vector dataset.
        input_dataset: Input dataset, potentially with sub-brick and/or\
            sub-range selectors.
        mask_dataset: Dataset to be used as a mask. Only voxels with nonzero\
            values in 'mset' will be averaged from 'dataset'. The mask dataset and\
            the input dataset must have the same number of voxels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dsvm_linpredict",
        "weight_vector": weight_vector,
        "input_dataset": input_dataset,
    }
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    return params


def v_3dsvm_linpredict_cargs(
    params: V3dsvmLinpredictParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("3dsvm_linpredict")
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    cargs.append(execution.input_file(params.get("weight_vector")))
    cargs.append(params.get("input_dataset"))
    return cargs


def v_3dsvm_linpredict_outputs(
    params: V3dsvmLinpredictParameters,
    execution: Execution,
) -> V3dsvmLinpredictOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dsvmLinpredictOutputs(
        root=execution.output_file("."),
        stdout_output=execution.output_file("stdout"),
    )
    return ret


def v_3dsvm_linpredict_execute(
    params: V3dsvmLinpredictParameters,
    execution: Execution,
) -> V3dsvmLinpredictOutputs:
    """
    Linear prediction for weights from 3dsvm.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dsvmLinpredictOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dsvm_linpredict_cargs(params, execution)
    ret = v_3dsvm_linpredict_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dsvm_linpredict(
    weight_vector: InputPathType,
    input_dataset: str,
    mask_dataset: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dsvmLinpredictOutputs:
    """
    Linear prediction for weights from 3dsvm.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        weight_vector: Weight vector dataset.
        input_dataset: Input dataset, potentially with sub-brick and/or\
            sub-range selectors.
        mask_dataset: Dataset to be used as a mask. Only voxels with nonzero\
            values in 'mset' will be averaged from 'dataset'. The mask dataset and\
            the input dataset must have the same number of voxels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dsvmLinpredictOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DSVM_LINPREDICT_METADATA)
    params = v_3dsvm_linpredict_params(
        mask_dataset=mask_dataset,
        weight_vector=weight_vector,
        input_dataset=input_dataset,
    )
    return v_3dsvm_linpredict_execute(params, execution)


__all__ = [
    "V3dsvmLinpredictOutputs",
    "V3dsvmLinpredictParameters",
    "V_3DSVM_LINPREDICT_METADATA",
    "v_3dsvm_linpredict",
    "v_3dsvm_linpredict_params",
]
