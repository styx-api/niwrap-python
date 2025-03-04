# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_DWITO_DT_METADATA = Metadata(
    id="edef0edb2012159a76d51a09912a5bd6c5660ab2.boutiques",
    name="3dDWItoDT",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dDwitoDtParameters = typing.TypedDict('V3dDwitoDtParameters', {
    "__STYX_TYPE__": typing.Literal["3dDWItoDT"],
    "gradient_file": InputPathType,
    "dataset": InputPathType,
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
        "3dDWItoDT": v_3d_dwito_dt_cargs,
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
        "3dDWItoDT": v_3d_dwito_dt_outputs,
    }.get(t)


class V3dDwitoDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dwito_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset"""


def v_3d_dwito_dt_params(
    gradient_file: InputPathType,
    dataset: InputPathType,
) -> V3dDwitoDtParameters:
    """
    Build parameters.
    
    Args:
        gradient_file: A 1D file of the gradient vectors with lines of ASCII\
            floats (Gxi, Gyi, Gzi) or a 1D file of b-matrix elements.
        dataset: A 3D bucket dataset with Np+1 sub-briks where the first\
            sub-brik is the volume acquired with no diffusion weighting.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dDWItoDT",
        "gradient_file": gradient_file,
        "dataset": dataset,
    }
    return params


def v_3d_dwito_dt_cargs(
    params: V3dDwitoDtParameters,
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
    cargs.append("3dDWItoDT")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("gradient_file")))
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_dwito_dt_outputs(
    params: V3dDwitoDtParameters,
    execution: Execution,
) -> V3dDwitoDtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dDwitoDtOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("<PREFIX>.*"),
    )
    return ret


def v_3d_dwito_dt_execute(
    params: V3dDwitoDtParameters,
    execution: Execution,
) -> V3dDwitoDtOutputs:
    """
    Computes 6 principal direction tensors from multiple gradient vectors and
    corresponding DTI image volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dDwitoDtOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_dwito_dt_cargs(params, execution)
    ret = v_3d_dwito_dt_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_dwito_dt(
    gradient_file: InputPathType,
    dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dDwitoDtOutputs:
    """
    Computes 6 principal direction tensors from multiple gradient vectors and
    corresponding DTI image volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        gradient_file: A 1D file of the gradient vectors with lines of ASCII\
            floats (Gxi, Gyi, Gzi) or a 1D file of b-matrix elements.
        dataset: A 3D bucket dataset with Np+1 sub-briks where the first\
            sub-brik is the volume acquired with no diffusion weighting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDwitoDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DWITO_DT_METADATA)
    params = v_3d_dwito_dt_params(
        gradient_file=gradient_file,
        dataset=dataset,
    )
    return v_3d_dwito_dt_execute(params, execution)


__all__ = [
    "V3dDwitoDtOutputs",
    "V3dDwitoDtParameters",
    "V_3D_DWITO_DT_METADATA",
    "v_3d_dwito_dt",
    "v_3d_dwito_dt_params",
]
