# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SUMA_ACKNOWLEDGE_METADATA = Metadata(
    id="3d8b17db995d67b601d4ce298b53b3fd6e31c716.boutiques",
    name="@suma_acknowledge",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VSumaAcknowledgeParameters = typing.TypedDict('VSumaAcknowledgeParameters', {
    "__STYXTYPE__": typing.Literal["@suma_acknowledge"],
    "input_file": InputPathType,
    "surface_file": InputPathType,
    "output_prefix": str,
    "center_flag": bool,
    "subsurface_file": typing.NotRequired[str | None],
    "scale_factor": typing.NotRequired[float | None],
    "reduce_factor": typing.NotRequired[float | None],
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
        "@suma_acknowledge": v__suma_acknowledge_cargs,
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
        "@suma_acknowledge": v__suma_acknowledge_outputs,
    }.get(t)


class VSumaAcknowledgeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_acknowledge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output graph dataset"""


def v__suma_acknowledge_params(
    input_file: InputPathType,
    surface_file: InputPathType,
    output_prefix: str,
    center_flag: bool = False,
    subsurface_file: str | None = None,
    scale_factor: float | None = None,
    reduce_factor: float | None = None,
) -> VSumaAcknowledgeParameters:
    """
    Build parameters.
    
    Args:
        input_file: Required input text file with format for each line: first\
            last groupname.
        surface_file: Required surface to place nodes.
        output_prefix: Output prefix for graph dataset.
        center_flag: Put center coord at x,y,z=0,0,0. Otherwise, uses average\
            xyz in surface.
        subsurface_file: Surface for surrounding members of group (use ld2,\
            ld4, ld5, ld6, .... default is ld5).
        scale_factor: Scale xyz for group nodes (default is 1.0).
        reduce_factor: Scale xyz offsets for member nodes (xyz/r), default is\
            10.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@suma_acknowledge",
        "input_file": input_file,
        "surface_file": surface_file,
        "output_prefix": output_prefix,
        "center_flag": center_flag,
    }
    if subsurface_file is not None:
        params["subsurface_file"] = subsurface_file
    if scale_factor is not None:
        params["scale_factor"] = scale_factor
    if reduce_factor is not None:
        params["reduce_factor"] = reduce_factor
    return params


def v__suma_acknowledge_cargs(
    params: VSumaAcknowledgeParameters,
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
    cargs.append("@suma_acknowledge")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-surf",
        execution.input_file(params.get("surface_file"))
    ])
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    if params.get("center_flag"):
        cargs.append("-center")
    if params.get("subsurface_file") is not None:
        cargs.extend([
            "-subsurf",
            params.get("subsurface_file")
        ])
    if params.get("scale_factor") is not None:
        cargs.extend([
            "-scalefactor",
            str(params.get("scale_factor"))
        ])
    if params.get("reduce_factor") is not None:
        cargs.extend([
            "-reducefactor",
            str(params.get("reduce_factor"))
        ])
    return cargs


def v__suma_acknowledge_outputs(
    params: VSumaAcknowledgeParameters,
    execution: Execution,
) -> VSumaAcknowledgeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSumaAcknowledgeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_prefix") + "_graph_dataset"),
    )
    return ret


def v__suma_acknowledge_execute(
    params: VSumaAcknowledgeParameters,
    execution: Execution,
) -> VSumaAcknowledgeOutputs:
    """
    Demo script to create a graph dataset to show names of individuals and groups,
    potentially useful for acknowledgements in a talk.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSumaAcknowledgeOutputs`).
    """
    params = execution.params(params)
    cargs = v__suma_acknowledge_cargs(params, execution)
    ret = v__suma_acknowledge_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__suma_acknowledge(
    input_file: InputPathType,
    surface_file: InputPathType,
    output_prefix: str,
    center_flag: bool = False,
    subsurface_file: str | None = None,
    scale_factor: float | None = None,
    reduce_factor: float | None = None,
    runner: Runner | None = None,
) -> VSumaAcknowledgeOutputs:
    """
    Demo script to create a graph dataset to show names of individuals and groups,
    potentially useful for acknowledgements in a talk.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Required input text file with format for each line: first\
            last groupname.
        surface_file: Required surface to place nodes.
        output_prefix: Output prefix for graph dataset.
        center_flag: Put center coord at x,y,z=0,0,0. Otherwise, uses average\
            xyz in surface.
        subsurface_file: Surface for surrounding members of group (use ld2,\
            ld4, ld5, ld6, .... default is ld5).
        scale_factor: Scale xyz for group nodes (default is 1.0).
        reduce_factor: Scale xyz offsets for member nodes (xyz/r), default is\
            10.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaAcknowledgeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_ACKNOWLEDGE_METADATA)
    params = v__suma_acknowledge_params(
        input_file=input_file,
        surface_file=surface_file,
        output_prefix=output_prefix,
        center_flag=center_flag,
        subsurface_file=subsurface_file,
        scale_factor=scale_factor,
        reduce_factor=reduce_factor,
    )
    return v__suma_acknowledge_execute(params, execution)


__all__ = [
    "VSumaAcknowledgeOutputs",
    "VSumaAcknowledgeParameters",
    "V__SUMA_ACKNOWLEDGE_METADATA",
    "v__suma_acknowledge",
    "v__suma_acknowledge_params",
]
