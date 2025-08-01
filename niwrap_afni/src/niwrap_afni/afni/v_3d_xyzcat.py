# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_XYZCAT_METADATA = Metadata(
    id="6187e73a39e2b8fe582b14ee9e2a4f3ca6740b27.boutiques",
    name="3dXYZcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dXyzcatParameters = typing.TypedDict('V3dXyzcatParameters', {
    "__STYXTYPE__": typing.Literal["3dXYZcat"],
    "direction": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "verbose": bool,
    "datasets": list[InputPathType],
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
        "3dXYZcat": v_3d_xyzcat_cargs,
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
        "3dXYZcat": v_3d_xyzcat_outputs,
    }.get(t)


class V3dXyzcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_xyzcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brainfile: OutputPathType | None
    """Output concatenated dataset."""
    output_headerfile: OutputPathType | None
    """Output concatenated dataset header."""


def v_3d_xyzcat_params(
    datasets: list[InputPathType],
    direction: str | None = None,
    prefix: str | None = None,
    verbose: bool = False,
) -> V3dXyzcatParameters:
    """
    Build parameters.
    
    Args:
        datasets: Input datasets to concatenate.
        direction: Catenate along direction 'Q' (X, Y, Z, or their synonyms I,\
            J, K).
        prefix: Use 'pname' for the output dataset prefix name.
        verbose: Print out some verbositiness as the program proceeds.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dXYZcat",
        "verbose": verbose,
        "datasets": datasets,
    }
    if direction is not None:
        params["direction"] = direction
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_xyzcat_cargs(
    params: V3dXyzcatParameters,
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
    cargs.append("3dXYZcat")
    if params.get("direction") is not None:
        cargs.extend([
            "-dir",
            params.get("direction")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    return cargs


def v_3d_xyzcat_outputs(
    params: V3dXyzcatParameters,
    execution: Execution,
) -> V3dXyzcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dXyzcatOutputs(
        root=execution.output_file("."),
        output_brainfile=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
        output_headerfile=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_xyzcat_execute(
    params: V3dXyzcatParameters,
    execution: Execution,
) -> V3dXyzcatOutputs:
    """
    Catenates datasets spatially.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dXyzcatOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_xyzcat_cargs(params, execution)
    ret = v_3d_xyzcat_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_xyzcat(
    datasets: list[InputPathType],
    direction: str | None = None,
    prefix: str | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dXyzcatOutputs:
    """
    Catenates datasets spatially.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Input datasets to concatenate.
        direction: Catenate along direction 'Q' (X, Y, Z, or their synonyms I,\
            J, K).
        prefix: Use 'pname' for the output dataset prefix name.
        verbose: Print out some verbositiness as the program proceeds.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dXyzcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_XYZCAT_METADATA)
    params = v_3d_xyzcat_params(
        direction=direction,
        prefix=prefix,
        verbose=verbose,
        datasets=datasets,
    )
    return v_3d_xyzcat_execute(params, execution)


__all__ = [
    "V3dXyzcatOutputs",
    "V3dXyzcatParameters",
    "V_3D_XYZCAT_METADATA",
    "v_3d_xyzcat",
    "v_3d_xyzcat_params",
]
