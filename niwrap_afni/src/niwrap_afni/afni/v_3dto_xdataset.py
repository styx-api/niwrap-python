# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DTO_XDATASET_METADATA = Metadata(
    id="9009e607061b1ff9ecff65e2bed0504b53b16aea.boutiques",
    name="3dtoXdataset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dtoXdatasetParameters = typing.TypedDict('V3dtoXdatasetParameters', {
    "__STYXTYPE__": typing.Literal["3dtoXdataset"],
    "prefix": str,
    "mask": InputPathType,
    "input_files": list[InputPathType],
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
        "3dtoXdataset": v_3dto_xdataset_cargs,
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
        "3dtoXdataset": v_3dto_xdataset_outputs,
    }.get(t)


class V3dtoXdatasetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dto_xdataset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_sdat: OutputPathType
    """Output file in .sdat format"""


def v_3dto_xdataset_params(
    prefix: str,
    mask: InputPathType,
    input_files: list[InputPathType],
) -> V3dtoXdatasetParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for the output file.
        mask: Mask dataset file.
        input_files: Input datasets to be converted.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dtoXdataset",
        "prefix": prefix,
        "mask": mask,
        "input_files": input_files,
    }
    return params


def v_3dto_xdataset_cargs(
    params: V3dtoXdatasetParameters,
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
    cargs.append("3dtoXdataset")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.append(execution.input_file(params.get("mask")))
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def v_3dto_xdataset_outputs(
    params: V3dtoXdatasetParameters,
    execution: Execution,
) -> V3dtoXdatasetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dtoXdatasetOutputs(
        root=execution.output_file("."),
        output_sdat=execution.output_file(params.get("prefix") + ".sdat"),
    )
    return ret


def v_3dto_xdataset_execute(
    params: V3dtoXdatasetParameters,
    execution: Execution,
) -> V3dtoXdatasetOutputs:
    """
    Convert input datasets to the format needed for 3dClustSimX.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dtoXdatasetOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dto_xdataset_cargs(params, execution)
    ret = v_3dto_xdataset_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dto_xdataset(
    prefix: str,
    mask: InputPathType,
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> V3dtoXdatasetOutputs:
    """
    Convert input datasets to the format needed for 3dClustSimX.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for the output file.
        mask: Mask dataset file.
        input_files: Input datasets to be converted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dtoXdatasetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DTO_XDATASET_METADATA)
    params = v_3dto_xdataset_params(
        prefix=prefix,
        mask=mask,
        input_files=input_files,
    )
    return v_3dto_xdataset_execute(params, execution)


__all__ = [
    "V3dtoXdatasetOutputs",
    "V3dtoXdatasetParameters",
    "V_3DTO_XDATASET_METADATA",
    "v_3dto_xdataset",
    "v_3dto_xdataset_params",
]
